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

**Index** - https://bzy-biz-sync.appspot.com/ | https://bzy-biz-sync.appspot.com/api/v1
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

 **Main Store Product Update Create Webhook** - https://bzy-biz-sync.appspot.com/api/v1/sync/product/main
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

 * **Notes:**

      _The main store product update and create webhooks trigger this to sync to biz site_

**Biz Store Product Update Create Webhook** - https://bzy-biz-sync.appspot.com/api/v1/sync/product/biz
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

* **Notes:**

     _The biz store product update and create webhooks trigger this to sync to biz site_

**GCP Sub Endpoint** - https://bzy-biz-sync.appspot.com/api/v1/sync
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

* **Notes:**

    _This receives the pushed messages from GCP topic_

## Built With

* [Flask/Flask Restful](https://flask-restful.readthedocs.io/en/latest/index.html) - The web framework used

* [Google Content Platform - App Engine](https://console.cloud.google.com/appengine?organizationId=563517976623&project=boozy-bundles) - Server Deployment

* [Google Content Platform - PubSub](https://console.cloud.google.com/cloudpubsub/topic/list?organizationId=563517976623&project=boozy-bundles) - Asynchronous Processing


## Versioning

Current Version: 1.0.0

## Authors

* **Emil Gamad** - *Initial work*
