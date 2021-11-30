from flask_restx import Resource, fields
from app import app, api

receiver_model = api.model(
    'Receiver',
    {'receiver': fields.String('Cisco is the best!')}
)


@api.route('/api/v1/info')
class Info(Resource):
    def get(self):
        """Return hardcoded info"""
        return {'Receiver': 'Cisco is the best!'}


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
