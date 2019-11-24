from blogapp.app import app

import blogapp.routes

app.run(host='0.0.0.0', port=5000, debug=True)