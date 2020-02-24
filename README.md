# Boozy Biz Sync API

This is the API for the Boozy Biz Sync used in syncing the Boozy Shopify Main Site and the Boozy Biz Shopify Site . Any changes in the main site overwrites the inventory of the biz site. Any sales in the biz site adjusts the inventory of the main site.

```
https://bzy-biz-sync.appspot.com/
```

## Installing

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

```
git clone https://github.com/boozy-ph/bzy-biz-sync.git
cd bzy-bundle-sync
virtualenv -p python3 .env
source .env/bin/activate
pip install -r requirements.txt
python main.py
```

## Deployment

These instructions will deploy the project to GCP app engine and production environment. Proceed with caution.

```
gcloud config configurations activate boozy-cities-ph
gcloud app deploy
```

## API Specifications

**Index** - https://github.com/boozy-ph/bzy-biz-sync.git | https://github.com/boozy-ph/bzy-biz-sync.git/api/v1
----

* **Method:**  `GET`

*  **URL Params**

   * **Required:** `None`

   * **Optional:**`None`

* **Data Params:**
    * `None`

* **Success Response:**

  * **Code:** 200
    **Content:** `{ Application: "Boozy Biz Sync API", Hello: "World"}`

* **Error Response:**

   * Errors always return 200 but are descriptive. Check GCP stacklogger for more details.

* **Notes:**

     _Index page of API_

**Renew Firebase Access Token** - https://bzy-cities-ph.appspot.com/api/v1/pyrebase/renew
  ----

  * **Method:**  `GET`

  *  **URL Params**

     * **Required:** `None`

     * **Optional:**`None`

  * **Data Params:**
      * `None`

  * **Success Response:**

    * **Code:** 200

  * **Error Response:**

     * Errors always return 200 but are descriptive. Check GCP stacklogger for more details.

  * **Sample Call:**

    https://bzy-cities-ph.appspot.com/api/v1/autocomplete?city=Makati

  * **Notes:**

    _Endpoint to trigger the renewal of the firebase access token. This is triggered by a cronjob every 55 minutes_

**Sync All Bundles** - https://bzy-cities-ph.appspot.com/api/v1/bundles/sync
----

  * **Method:**  `POST`

  *  **URL Params**

     * **Required:** `None`

     * **Optional:**`None`

  * **Data Params:**
      * `None`

  * **Success Response:**

    * **Code:** 200
    * **Content:*** {"sync_status_id": bundle_id}

  * **Error Response:**

     * Errors always return 200 but are descriptive. Check GCP stacklogger for more details.

  * **Sample Call:**

    https://bzy-cities-ph.appspot.com/api/v1/bundles/sync

  * **Notes:**

    _Endpoint to trigger the process to sync all the bundles in the boozy-bundle firestore_

**Publish Sync Bundles** - https://bzy-cities-ph.appspot.com/api/v1/bundles/async
----

  * **Method:**  `POST`

  *  **URL Params**

     * **Required:** `None`

     * **Optional:**`None`

  * **Data Params:**
      * `List of Bundle IDs`

  * **Success Response:**

    * **Code:** 200
    * **Content:*** [List of ids]

  * **Error Response:**

     * Errors always return 200 but are descriptive. Check GCP stacklogger for more details.

  * **Sample Call:**

    https://bzy-cities-ph.appspot.com/api/v1/bundles/sync

    ```
    payload: {[bundle_id_1, bundle_id_2, bundle_id_3]}
    ```

  * **Notes:**

    _Endpoint to publish list of bundle ids to sync in firebase_

**Process Sync Bundles** - https://bzy-cities-ph.appspot.com/api/v1/bundles/run
----

  * **Method:**  `POST`

  *  **URL Params**

     * **Required:** `None`

     * **Optional:**`None`

  * **Data Params:**
      * `None`

  * **Success Response:**

    * **Code:** 200

  * **Error Response:**

     * Errors always return 200 but are descriptive. Check GCP stacklogger for more details.

  * **Sample Call:**

    https://bzy-cities-ph.appspot.com/api/v1/bundles/run

  * **Notes:**

    _Endpoint that receives published messages from GCP topic and syncs bundle ids_

## Built With

* [Flask/Flask Restful](https://flask-restful.readthedocs.io/en/latest/index.html) - The web framework used

* [Google Content Platform - App Engine](https://console.cloud.google.com/appengine?organizationId=563517976623&project=boozy-bundles) - Server Deployment

* [Google Content Platform - PubSub](https://console.cloud.google.com/cloudpubsub/topic/list?organizationId=563517976623&project=boozy-bundles) - Asynchronous Processing


## Versioning

Current Version: 1.0.0

## Authors

* **Emil Gamad** - *Initial work*
