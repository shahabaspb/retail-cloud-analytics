import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import pyspark.sql.functions as F

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read data from S3
df = spark.read.csv("s3://your-bucket/raw_sales_data.csv", header=True, inferSchema=True)

# Data transformation
df_cleaned = df.withColumn("Revenue", df["Revenue"].cast("double"))

# Write back to S3 in Parquet
df_cleaned.write.mode("overwrite").parquet("s3://your-bucket/processed_sales_data/")

job.commit()
