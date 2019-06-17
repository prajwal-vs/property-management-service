#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from flask import request
from flask_restful import Resource

from services.propertyManagement import PropertyService


class BuildingAddition(Resource):

    def __init__(self):
        self.service = PropertyService()

    def post(self):
        """Adding Building Details."""
        data = json.loads(request.data)

        output = self.service.create_building_details(data)
        return output

    def get(self):
        """Building List."""

        # limit = request.args.get("limit", 10)
        # offset = request.args.get("offset", 0)
        # keyword = request.args.get("keyword", "")
        # sort_field = request.args.get("sort_field", "updated_at")

        result = self.service.get_list_building("buildings")

        return result

    def delete(self):
        """ Bulk Delete Building Details """
        data = json.loads(request.data.decode('utf-8'))
        ids = data['ids']

        datastores = self.service.bulk_delete_buildings(ids)
        return datastores
