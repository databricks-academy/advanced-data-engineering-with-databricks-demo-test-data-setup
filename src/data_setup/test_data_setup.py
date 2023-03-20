class test_data:
    def __init__(self):
        self.bpm_json = """{"device_id":161910,"time":"2019-12-01T11:57:31.000+0000","heartrate":68.64985536254405}
{"device_id":142838,"time":"2019-12-01T11:58:03.000+0000","heartrate":73.42208600878647}
{"device_id":124880,"time":"2019-12-01T11:58:03.000+0000","heartrate":75.97373066574369}
{"device_id":134009,"time":"2019-12-01T11:58:20.000+0000","heartrate":79.77338592716501}
{"device_id":null,"time":"2019-12-01T11:58:33.000+0000","heartrate":67.91460485184962}
{"device_id":109290,"time":"2019-12-01T11:58:33.000+0000","heartrate":null}
{"device_id":193806,"time":"2019-12-01T11:58:34.000+0000","heartrate":-69.6489747665297}
{"device_id":"Tracker #161910","time":"2019-12-01T11:58:42.000+0000","heartrate":65.3691488917709}"""

        self.workouts_json = """{"user_id":25477,"workout_id":9,"timestamp":1576482430,"action":"stop","session_id":9}
{"user_id":25143,"workout_id":21,"timestamp":1576501500,"action":"start","session_id":7}
{"user_id":41732,"workout_id":24,"timestamp":1576505220,"action":"start","session_id":7}
{"user_id":49296,"workout_id":33,"timestamp":1576506500,"action":"stop","session_id":69}
{"user_id":40872,"workout_id":null,"timestamp":1576507900,"action":"start","session_id":101}
{"user_id":16093,"workout_id":27,"timestamp":1576508670,"action":null,"session_id":508}
{"user_id":14633,"workout_id":42,"timestamp":1576508160,"action":"stop","session_id":"FIRST_SESSION"}"""
    
        self.users_cdc_json = """{ "user_id": 31362, "update_type": "new", "timestamp": 1555539580, "dob": "02/01/2001", "sex": "F", "gender": "F", "first_name": "Shelley", "last_name": "Andrews", "address": {"street_address":"4791 Nathan Turnpike Suite 540","city":"Los Angeles","state":"CA","zip":90024} }
{ "user_id": 31362, "update_type": "update", "timestamp": 1555539580, "dob": "02/02/2001", "sex": "F", "gender": "F", "first_name": "Andrew", "last_name": "Shelley", "address": {"street_address":"4791 Nathan Turnpike Suite 540","city":"Los Angeles","state":"CA","zip":90024} }
{ "user_id": 33987, "update_type": "new", "timestamp": 1559688700, "dob": "05/10/1965", "sex": "F", "gender": "F", "first_name": "Jennifer", "last_name": "Perez", "address": {"street_address":"973 Norman Mountain Apt. 290","city":"Canyon Country","state":"CA","zip":91386} }
{ "user_id": 45875, "update_type": "new", "timestamp": 1565615100, "dob": "12/13/1933", "sex": "M", "gender": "M", "first_name": "Christopher", "last_name": "Juarez", "address": {"street_address":"696 Justin Crest Apt. 656","city":"El Monte","state":"CA","zip":91731} }
{ "user_id": 45875, "update_type": "new", "timestamp": 1565615100, "dob": "12/13/1933", "sex": "M", "gender": "M", "first_name": "Christopher", "last_name": "Juarez", "address": {"street_address":"696 Justin Crest Apt. 656","city":"El Monte","state":"CA","zip":91731} }
{ "user_id": null, "update_type": "new", "timestamp": 1557990020, "dob": "11/19/1944", "sex": "M", "gender": "M", "first_name": "Joshua", "last_name": "Mitchell", "address": {"street_address":"843 Hannah Corners","city":"Woodland Hills","state":"CA","zip":91367} }
{ "user_id": 41954, "update_type": null, "timestamp": 1563474300, "dob": "01-05-1964", "sex": "F", "gender": "F", "first_name": "Sandra", "last_name": "Flores", "address": {"street_address":"203 Nicholson Mountains","city":"Glendale","state":"CA","zip":91201} }
{ "user_id": "#36644", "update_type": "new", "timestamp": 1566185600, "dob": "03/07/1941", "sex": "M", "gender": "M", "first_name": "Casey", "last_name": "Miles", "address": {"street_address":"27548 Craig Dale Apt. 118","city":"Altadena","state":"CA","zip":91001} }"""

    def get_data_description(self):
        return """There are three datasets in this repository:
        
        1. bpm_json
            - Schema: device_id LONG, time TIMESTAMP, heartrate DOUBLE
            - 4 normal records
            - 1 record with null device_id
            - 1 record with null heartrate
            - 1 record with negative heartrate
            - 1 record with incompatible schema (invalid string for device_id)
            
        2. workouts_json
            - Schema: `user_id INT, workout_id INT, timestamp FLOAT, action STRING, session_id INT`
            - 3 normal workout records
            - 1 workout record with null workout ID
            - 1 workout record with null action
            - 1 workout record with incompatible schema (invalid string for session_id)

        3. users_cdc_json
            - Schema: user_id LONG, update_type STRING, timestamp FLOAT, dob STRING, sex STRING, gender STRING, first_name STRING, last_name STRING, address STRUCT<street_address: STRING, city: STRING, state: STRING, zip: INT>
            - 4 normal records
            - 1 duplicate record
            - 1 null user_id
            - 1 null update_type
            - 1 record wth incompatible schema (invalid string for user_id)
        """            
