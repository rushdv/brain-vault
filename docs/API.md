# Brain Vault API Documentation

## Base URL
- Development: `http://localhost:8000`
- Production: `https://api.brain-vault.com` (when deployed)

## Endpoints

### Health Check
```
GET /health
```
Returns the health status of the API.

**Response:**
```json
{
  "status": "healthy"
}
```

### Get Data
```
GET /api/data
```
Returns sample data from the backend.

**Response:**
```json
{
  "message": "Hello from FastAPI Backend!",
  "status": "success"
}
```

## Authentication
Currently, no authentication is required. This will be added in future versions.

## Error Handling
All errors follow this format:
```json
{
  "detail": "Error message",
  "status_code": 400
}
```

## Rate Limiting
Rate limiting will be implemented in future versions.

## CORS
The API accepts requests from:
- `http://localhost:5173` (local frontend)
- `https://brain-vault-iota.vercel.app` (production frontend)

## API Documentation
Interactive API documentation is available at:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## Versioning
Current API version: `1.0.0`

Future versions will use URL versioning: `/api/v2/...`
