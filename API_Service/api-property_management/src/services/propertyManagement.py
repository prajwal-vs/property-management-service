# ------------------------------------------------------------------------------
# CUSTOM FUNCTION IMPORTS
# ------------------------------------------------------------------------------


import datetime
import json
import uuid

from flask import request
# ------------------------------------------------------------------------------
# PYMONGO FEATURES IMPORT
# ------------------------------------------------------------------------------
from pymongo.errors import PyMongoError

from commons.json_utils import to_json, to_list_json
from commons.mongo_services import MongoClients, DB_NAME
from constants.custom_field_error import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_201_CREATED, \
    HTTP_203_NON_AUTHORITATIVE_INFORMATION


class PropertyService:
    """Login Service"""

    def __init__(self):
        """Init.

        method is run as soon as an object of a class is instantiated.
        The method is useful to do any initialization you want to do
        with your object
        """
        self.connection = MongoClients()
        self.error = None
        self.error_code = None

    def create_building_details(self, data):
        """Add building Details."""

        data_ext = {
            'name': str(data['name']),
            'address': str(data['address']),
            'contact_no': data['contact_no'],
            'landmark': str(data['landmark']),
            'building_id': str(uuid.uuid4()),
            'owner': str('unknown'),
            'total_floors': data['floors'],
            'created_at': str(datetime.datetime.now()),
            'created_by': request.headers.get("userName", "unknown"),
            'updated_at': str(datetime.datetime.now())

        }

        try:

            response = self.connection.insert_one(
                collectionname="buildings",
                data=json.dumps(data_ext))
            return to_json({"message": "Building details added Successfully"}, is_error=True), HTTP_201_CREATED

        except PyMongoError as err:
            return to_json({"message": err.args[0]}, is_error=True), HTTP_500_INTERNAL_SERVER_ERROR

    def get_list_building(self, collectionname):
        try:
            data, result_count = self.connection.find_all(db_name=DB_NAME,
                                                          collection_name=collectionname)
            for lst in data:
                lst.pop("_id")
            return to_list_json(data, list_count=result_count)
        except PyMongoError as err:
            return to_json({"message": err.args[0]}, is_error=True), HTTP_500_INTERNAL_SERVER_ERROR

    def add_room_details(self, data, building_id):
        """Add Room Details"""

        data_ext = {
            'flat_number': data['flat_number'],
            'square_feet_area': data['square_feet_area'],
            'rent': data['rent'],
            'room_id': str(uuid.uuid4()),
            'building_id': building_id,
            'type': str(data['type']),
            'no_of_bathrooms': data['no_of_bathrooms'],
            'maintenance_charge': data['maintenance_charge'],
            'electricity_acc_no': str(data['electricity_acc_no']),
            'created_at': str(datetime.datetime.now())
        }

        try:
            # return_object = self.connection.find_one(
            #     collectionname="rooms",
            #     data={"room_id": data['room_id']}
            # )
            #
            # if return_object:
            #     return to_json({"message": "Room Details Already Exist"},
            #                    is_error=True), HTTP_203_NON_AUTHORITATIVE_INFORMATION

            response = self.connection.insert_one(
                collectionname="rooms",
                data=json.dumps(data_ext))
            return to_json({"message": "Room details added Successfully"}, is_error=True), HTTP_201_CREATED

        except PyMongoError as err:
            return to_json({"message": err.args[0]}, is_error=True), HTTP_500_INTERNAL_SERVER_ERROR

    def get_list_room(self, collectionname, querydata):
        try:
            data, result_count = self.connection.find_all(db_name=DB_NAME,
                                                          collection_name=collectionname,
                                                          query=querydata)
            return to_list_json(data, list_count=result_count)
        except PyMongoError as err:
            return to_json({"message": err.args[0]}, is_error=True), HTTP_500_INTERNAL_SERVER_ERROR

    def get_building(self, id):
        output, count = self.connection.find(DB_NAME, 'buildings', {'building_id': id})
        result = {}
        for service in output:
            result = service
            del result['_id']
        return to_json(result)

    def delete_building(self, id):
        result = self.connection.find_one_and_delete(DB_NAME, 'buildings', {'building_id': id})
        return to_json(result)

    def update_building(self, newObj, id):
        output = self.connection.find_one_and_update(DB_NAME, 'buildings', {'building_id': id},
                                                     {'$set': newObj})
        del output['_id']
        return to_json(output)

    def bulk_delete_buildings(self, ids):
        results = []
        try:
            for id in ids:
                result = s.find_one_and_delete(self.db_name, self.collection_name,
                                               {'transporter_id': id})
                results.append(id)
        except PyMongoError as err:
            logger.error(err)
            return to_json({"message": err.args[0]}, is_error=True), HTTP_500_INTERNAL_SERVER_ERROR
        return to_json(results)
