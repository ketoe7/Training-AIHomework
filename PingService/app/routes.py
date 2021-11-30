from flask_restx import Resource, fields
import requests
from json.decoder import JSONDecodeError
from app import app, api

ping_model = api.model(
    'Url',
    {
        'url': fields.String('https://receiver-service:8080.com')
    }
)

health_model = api.model(
    'Health',
    {
        'status': fields.String('healthy')
    }
)


@api.route('/api/v1/health')
class Health(Resource):

    def get(self):
        """Healthcheck for the service."""
        return {'status': 'healthy'}


@api.route('/api/v1/ping')
class Ping(Resource):

    @api.expect(ping_model)
    @api.response(200, f'Host is reachable')
    @api.response(400, f'Host is not reachable')
    def post(self):
        """Send GET request to the given url."""
        try:
            response = requests.get(api.payload['url'], verify=False)
            response.raise_for_status()
        except requests.ConnectionError as err:
            return {
                'error': f'Connection error while trying to send GET '
                         f'request to {api.payload["url"]}. '
                         f'Are you sure the URL is correct?',
                'message': str(err)
            }, 400
        except requests.Timeout as err:
            return {
                'error': f'Timeout occurred while trying to send GET '
                         f'request to {api.payload["url"]}',
                'message': str(err)
            }, 400
        except requests.exceptions.HTTPError as err:
            return {
                'error': f'{api.payload["url"]} responded with HTTP error',
                'message': str(err)
            }, 400
        except Exception as err:
            return {
                'error': f'Unknown error while trying to send GET '
                         f'request to {api.payload["url"]}',
                'message': err
            }, 400
        else:
            try:
                result = response.json()
            except JSONDecodeError:
                return {'body': str(response.text)}
            else:
                return result, 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
