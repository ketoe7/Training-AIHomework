from flask_restx import Resource, fields
from app import app, api

receiver_model = api.model(
    'Receiver',
    {'receiver': fields.String('Cisco is the best!')}
)


@api.route('/api/v1/info')
class Info(Resource):
    # @api.marshal_with(receiver_model, code=200)
    def get(self):
        """Healthcheck for the service."""
        return {'Receiver': 'Cisco is the best!'}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
