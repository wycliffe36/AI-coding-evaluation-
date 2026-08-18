## [API-19] /users endpoint times out under load

### Description
The new /users endpoint works for 1 request but freezes when hit 3 times at once. 
Logs show "Task was destroyed but it is pending"

### Steps to Reproduce
`uvicorn app.api:app --reload` then hit /users 3 times quickly

### Expected Behavior
Endpoint returns JSON in <100ms even with concurrent requests

### Actual Behavior
Server hangs and eventually returns 500

### Constraints
- Use aiosqlite instead of sqlite3
- Do NOT change the endpoint path or return format
- Must pass pytest
