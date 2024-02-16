Flask Framework
Using the Application Factory Pattern
________________________________________________________


TO RUN VIRTUAL ENVIRONMENT:
Navigate to root directory and paste ENTIRE LINE:
source venv/bin/activate

________________________________________________________


TO RUN APP:
Navigate to root directory. Set FLASK_CONFIG environment
variable by running the following commands in Terminal:

FOR DEVELOPMENT:
export FLASK_CONFIG=DevelopmentConfig
# or
FOR PRODUCTION:
export FLASK_CONFIG=ProductionConfig

THEN:
To run entire application, navigate to root and paste:
python3 run.py


NOTE:
The export command sets the environment variable for the current terminal session only. If you open a new terminal window or session, you'll need to set the environment variable again.

________________________________________________________