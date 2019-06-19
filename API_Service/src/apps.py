#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Flask base application declaration and URL configuration."""

from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from resources.building import Building
from resources.buildingAddition import BuildingAddition
from resources.roomAddition import RoomAddition
from resources.roomList import RoomList

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['PROPAGATE_EXCEPTIONS'] = True

# ------------------------------------------------------------------------------
# Property Management Services
# ------------------------------------------------------------------------------

# http://server/api/v1/add_building
api.add_resource(BuildingAddition, '/api/v1/building')

# http://server/api/v1/add_building
api.add_resource(Building, '/api/v1/building/<string:building_id>')

# http://server/api/v1/add_rooms
api.add_resource(RoomAddition, '/api/v1/<string:building_id>/add_rooms')

# http://server/api/v1/{building_id}/all
api.add_resource(RoomList, '/api/v1/<string:building_id>/all')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
