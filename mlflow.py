import mlflow

with mlflow.start_run():

    # Log basic parameters
    mlflow.log_param("user", "customer_1")
    mlflow.log_param("order_item", "Pizza")

    # Log system metrics
    mlflow.log_metric("order_value", 250)
    mlflow.log_metric("delivery_time", 30)

    print("MLflow tracking done")

