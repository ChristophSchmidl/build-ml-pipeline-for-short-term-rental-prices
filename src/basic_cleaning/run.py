#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # Custom code begins #
    ######################
    
    # 4. Save the results to a CSV file called clean_sample.csv (df.to_csv("clean_sample.csv", index=False)). 
    # NOTE: Remember to use index=False when saving to CSV, otherwise the data checks in the next step might fail because there will be an extra index column. 

    min_price = args.min_price
    max_price = args.max_price

    output_artifact = args.output_artifact
    output_type = args.output_type
    output_description = args.output_description

    logger.info(f"Min price: {min_price}")
    logger.info(f"Max price: {max_price}")

    logger.info(f"Output artifact: {output_artifact}")
    logger.info(f"Output type: {output_type}")
    logger.info(f"Output description: {output_description}")

    
    logger.info("Downloading the data from W&B...")
    local_path = wandb.use_artifact("sample.csv:latest").file()
    df = pd.read_csv(local_path)


    logger.info("Drop outliers...")
    idx = df['price'].between(min_price, max_price)
    df = df[idx].copy()
    # Convert last_review to datetime
    df['last_review'] = pd.to_datetime(df['last_review'])

    idx = df['longitude'].between(-74.25, -73.50) & df['latitude'].between(40.5, 41.2)
    df = df[idx].copy()


    logger.info("Save cleaned dataframe to CSV file: clean_sample.csv")
    df.to_csv("clean_sample.csv", index=False)

    artifact = wandb.Artifact(
     output_artifact,
     type=output_type,
     description=output_description,
    )

    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)

    ######################
    # Custom code ends #
    ######################



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="Input artifact",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Output artifact",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="Output type",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="Output description",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="Min price",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="Max price",
        required=True
    )


    args = parser.parse_args()

    go(args)
