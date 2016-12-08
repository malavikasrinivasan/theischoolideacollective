import os
from app import app
port = int(os.environ.get('PORT', 8081))
app.run(debug=True, host="localhost", port=port)
