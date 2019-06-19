#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import json

from flask import request
from flask_restful import Resource

from services.propertyManagement import PropertyService


class Building(Resource):

    def __init__(self):
        self.service = PropertyService()

    def get(self, building_id):
        """ Get  """
        response = self.service.get_building(building_id)
        return response

    def delete(self, building_id):
        """ Delete """
        response = self.service.delete_building(building_id)
        return response

    def put(self, building_id):
        """ Update """
        data = json.loads(request.data.decode('utf-8'))
        # data['updated_at'] = str(datetime.datetime.utcnow())
        update_response = self.service.update_building(data, building_id)
        return update_response
