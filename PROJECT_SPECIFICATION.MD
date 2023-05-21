# Project specification

## W&B Set-Up

| Criteria  | Meets specifications  |
|---|---|
| Public W&B project ``nyc_airbnb``  | Your W&B project nyc_airbnb should be made public, so that your reviewer can access it. This is needed so the reviewer can check that the W&B steps have been executed successfully. <br><br> **Make sure the link to your W&B project, as well as your Github repository (i.e. two links), are included in a README file or given to the reviewer in the "Submission Details" box you can use when initiating the submission process.**  |

## Exploratory Data Analysis

| Criteria  | Meets specifications  |
|---|---|
| Obtain sample data | There is a sample.csv artifact in W&B.<br><br>The pipeline has been run to get a sample of the data, which has been uploaded to W&B. |
| Utilize an EDA notebook  | There is a notebook called EDA in the students’ repository (most probably in the src/eda directory).<br><br>The EDA notebook contains a properly formatted Jupyter notebook with comments and markdown cells.  |
| Fetch data into the notebook  | At the beginning of the notebook, fetch the sample.csv artifact from W&B.  |
| Clean the sample data  | The data is clean at the end of the notebook. Note that there will still be some missing entries, because we are not imputing missing values.<br><br>Properly implemented the checks suggested in the ``notes.md`` file.   |

## Data Cleaning

| Criteria  | Meets specifications  |
|---|---|
| Create a “basic_cleaning” step in the Github repository | There is a new “basic_cleaning” step in the Github repository (under the src directory).<br><br>The basic_cleaning step respects the MLFlow structure: a conda.yml, a MLproject and a python script. It has the parameters input_artifact, output_name, output_type, output_description, min_price and max_price.  |
| Update the ``conda.yml`` file  | The conda.yml file has been updated to add the ``pandas`` dependency. |
| Update all parameters | Add docstrings and the proper type to all parameters, both in the script and in the MLproject file. |
| Run basic_cleaning without errors  | The basic_cleaning step re-implements in a MLFlow step the data cleaning you performed during the EDA. It should be added to the main.py file and run without errors.<br><br>In the main.py file all parameters are taken from the configuration file, and not hard-coded. |
| Create clean_data.csv in W&B | At the end of the run of this step, there should be a clean_data.csv artifact uploaded to W&B. |

## Data Testing

| Criteria  | Meets specifications  |
|---|---|
| Create a “reference” tag for the latest version of the clean_sample.csv artifact | In W&B, manually add a tag called “reference” to the latest version of the clean_sample.csv artifact. |
| Implement the ``test_row_count`` and the test_price_range tests in ``src/data_check/test_data.py`` | Implements the ``test_row_count`` and the test_price_range tests in ``src/data_check/test_data.py``.<br><br>The added tests are checking respectively for a proper size of the dataset, and for a proper price range. |
| The pipeline runs successfully | The pipeline runs after this step, and all the tests pass. |

## Data Splitting

| Criteria  | Meets specifications  |
|---|---|
| Split data into training, validation and test sets. | Adds the train_val_test_split component to the main.py file.<br><br>The train_val_test_split has been provided to you. You can just add it to the main.py file and fill in the parameters appropriately. |
| The pipeline again runs successfully | The pipeline runs. At the end there should be 2 new artifacts on W&B: ``trainval_data.csv``, ``test_data.csv``. |

## Train the Random Forest

| Criteria  | Meets specifications  |
|---|---|
| Complete the ``src/train_random_forest/run.py`` script | The ``src/train_random_forest/run.py`` script is completed.<br><br>When checking the script, there should be the following steps in the script, marked by clear comments:<br><br>1. Download the train data using W&B.<br>2. In the get_inference_pipeline function, implement a pipeline called ``non_ordinal_categorical_preproc`` with two steps: a ``SimpleImputer(strategy="most_frequent")`` and a ``OneHotEncoder()`` step<br>3. In the ``get_inference_pipeline`` function, create the inference pipeline called ``sk_pipe`` containing the preprocessing step and the Random Forest<br>4. In the go function, fit the pipeline.<br>5. In the go function, export the pipeline using MLFlow model export.<br>6. Upload the artifact to W&B<br>7. Log the variable MAE to W&B |
| The pipeline again runs successfully | The pipeline again runs successfully.<br><br>The ``train_random_forest`` step is added to the ``main.py`` file. |
| Create the model_export artifact on W&B | There should be an artifact created on W&B called model_export.<br><br>The model_export artifact should contain a MLflow sklearn serialized model. |

## Optimize Hyperparameters

| Criteria  | Meets specifications  |
|---|---|
| Run training with different hyperparameters | Using the Hydra system, run a hyper-parameter search.<br><br>On W&B there should be the results of several (>2) training jobs with different hyperparameters. |

## Select the Best Model

| Criteria  | Meets specifications  |
|---|---|
| Select the best performing model and tag it as “prod” | Add the tag “prod” to the trained model with the best MAE. |

## Test Set Verification

| Criteria  | Meets specifications  |
|---|---|
| Verify test set performance is comparable to performance on the validation set (no overfitting) | Implement the ``test_regression_model`` function in the ``main.py`` file. The test_regression_model is provided just as in the “data splitting” step.<br><br>Verify that the performance is comparable to what was obtained against the validation set (i.e. no overfitting occurred). |

## Visualize the Pipeline

| Criteria  | Meets specifications  |
|---|---|
| Visualize the pipeline and verify proper structure | Navigate to W&B, to the artifact section, then click on “Graph view”. The resulting visualization should show the pipeline properly organized. Refer to the reference plot in notes.md. |

## Release the Pipeline

| Criteria  | Meets specifications  |
|---|---|
| Release v1.0.0 of the pipeline in Github | A release of the pipeline is cut from the Github repository, with version 1.0.0 or similar (if you need more trials, you might assign versions like 1.0.1 or 1.0.2, which is totally fine). |

## Train the Model on a New Data Sample

| Criteria  | Meets specifications  |
|---|---|
| Run the released pipeline on a new sample of data, with initial failure | Run the released pipeline on a new sample of data, sample2.csv. The first version 1.0.0 (or similar) should fail, because there is a data problem in sample2.csv. |
| Add a new cleaning step in basic_cleaning | Implement a new cleaning step that removes data points that are outside of the area of NYC in ``basic_cleaning``. |
| Prepare a new release | After adding the new cleaning step and committing and pushing to the repository, release a new version (for example, 1.0.1). |
| Run the new release successfully | Re-running with the new release should produce a new trained model. |


## Suggestions to make your project stand out!

1. In the data exploration step, you can go far beyond what is shown here, such as including visualizations and other data cleaning steps. This should allow you to get even better performance from the model.
2. Explore other models beyond the RandomForest trained here, creating a new separate step or customizing the random forest one to accommodate different types of models.
3. Add discussion to a README file concerning other changes you might consider in future releases of your pipeline.