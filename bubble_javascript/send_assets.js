/*
    This JavaScript code is utilized in Step/Action 2 within 
    the "Run JavaScript" plugin as part of 
    the "Python Calculate Stats" custom event in Bubble.

    It performs two primary functions:

    1. Compiles the list of assets retrieved from 
    the custom state set in Step/Action 1 into a JSON array. 
    This array is then structured to be compatible with 
    the expected format for the Python backend.

    2. Initiates an API POST request, embedding the 
    compiled JSON array in the body of the request. 
    This operation facilitates the transmission of 
    asset data from Bubble to the Python backend to the
    stats/portfolio_stats endpoint.

    *** IMPORTANT ***
    THE AUTHORIZATION SECRET CODE IS INTENTIONALLY
    REMOVED FROM THIS .JS FILE. IF YOU COPY/PASTE YOU
    WILL NEED TO REPLACE THE AUTHORIZATION CODE
*/

var assetsList = [BUBBLEEXPRESSION]; // Assuming this is now correctly an array of objects
console.log("Assets List (Before Parsing):", assetsList);

// No need to parse assetsList as it's already the correct format
var compiledAssets = assetsList.map(function(asset) {
    return {
        symbol: asset.Symbol,
        equity: parseFloat(asset.Equity), // Convert the string 'Equity' to a floating-point number
        group_assignment: asset["Group Assignment"]
    };
});

var compiledAssetsJson = JSON.stringify(compiledAssets);
console.log("Compiled Assets JSON:", compiledAssetsJson);


var compiledAssetsJson = JSON.stringify(compiledAssets);
console.log("Compiled Assets JSON:", compiledAssetsJson);

// Now, send the API POST request with compiledAssetsJson as the body
fetch('https://api.portfoliomatrix.com/stats/portfolio_stats', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': '[CODE]'
    },
    body: compiledAssetsJson
})
.then(response => response.json())
.then(data => {
    console.log("API Response:", data);
})
.catch(error => console.error('Error:', error));


/*
THE FOLLOWING IS THE FORMAT FOR THE "BUBBLEEXPRESSION" DYNAMIC DATA:

dashboard's Compile Assets for Python:format as text

WHERE
dashboard = page for custom state
Compile Assets for Python = custom state that stores assets

FORMAT AS TEXT:
{"Symbol":"This Asset's Symbol", "Equity": "This Asset's Equity", "Group Assignment": "This Asset's Group Assignment's Group Name"}

Delimiter:
,

*** IMPORTANT ***
USE THE EXACT "FORMAT AS TEXT" to create JSON arrays
*/







// BELOW IS FUNCTIONAL BUBBLE PLUGIN CODE FOR THE SERVER SIDE POST REQUEST


function(properties, context) {
    // Log the properties to diagnose the issue
    console.log('properties:', properties);

    // Initialize the array to compile the data
    let assetsArray = [];

    // Ensure 'properties.asset' is defined and is an array before proceeding
    if (Array.isArray(properties.asset)) {
        // Loop through the 'properties.asset' property
        properties.asset.forEach(item => {
            // Convert 'equity' from string to float and ensure 'symbol' and 'group_assignment' are defined
            let equityValue = parseFloat(item.value); // Convert equity to float
            if (!isNaN(equityValue)) { // Check if the conversion is successful
                assetsArray.push({
                    "symbol": item.key, 
                    "equity": equityValue, // Use the converted float value
                    "group_assignment": item.group 
                });
            } else {
                console.error("Failed to convert equity to float for item:", item);
                // Handle the case where conversion fails, e.g., skip the item or set a default value
            }
        });
    } else {
        // Handle the case where 'properties.asset' is not as expected
        throw new Error("'properties.asset' is not an array or is undefined.");
    }

    // Prepare the request options
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': '9e83b67c-bd1e-4c50-a6d8-f1e1137b8428'
        },
        body: JSON.stringify(assetsArray)
    };

    // Assuming 'fetch' is available in the server-side environment
    return fetch('https://a1d35ea4-b208-4439-8824-5fba42dc2c8e.mock.pstmn.io', requestOptions)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            // Structure the response with 'text_response_json' as a key
            return { 'text_response_json': JSON.stringify(data) };
        })
        .catch(error => {
            console.error('There has been a problem with your fetch operation:', error);
            throw new Error(error.message);
        });
}
