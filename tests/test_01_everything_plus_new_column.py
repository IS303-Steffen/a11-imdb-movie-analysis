max_score = 33  # This value is pulled by yml_generator.py to assign a score to this test.
from conftest import (
    normalize_text,
    load_student_code,
    format_error_message,
    exception_message_for_students,
    record_failure,
    get_similarity_feedback,
    pc_get_or_create,
    pc_finalize_and_maybe_fail,
    default_module_to_test,
)
import os

# Checks if the expected printed messages actually appear, but doesn't check for specific inputs or correct calculations.
def test_01_everything_plus_new_column(current_test_name):
    try:
        try:
            import pandas as pd
        except ImportError:
            exception_message_for_students(ImportError("This test requires the pandas library being installed on your computer, but pandas is not installed"), input_test_case=None, current_test_name=current_test_name) 
        
        rec = pc_get_or_create(current_test_name, max_score=max_score)
        CURRENT_DIR = os.path.dirname(__file__)
        pickle_file_path = os.path.join(CURRENT_DIR, '01.xlsx')
        # Expected data
        expected_data = pd.read_excel(pickle_file_path)
        expected_data.query("index ==16", inplace=True)
        
        expected_data_str = expected_data.iloc[0].to_string(index=False)

        # load the code to make sure it generates the needed file:
        load_student_code(current_test_name, inputs = [])

        expected_file_name = r"everything_plus_new_column.xlsx"

        if not os.path.isfile(expected_file_name):
            formatted = format_error_message(
                custom_message=(
                    f"This test is looking for this file:\n"
                    f"```\n{expected_file_name}\n```\n"
                    f"But it couldn't find it. Make sure you are creating this file "
                    f"and spelling it correctly."),
                current_test_name=current_test_name
            )
            record_failure(current_test_name, formatted_message=formatted, input_test_case=None, reason="couldn't find file")
            return  # allow finalizer to handle overall failure
    
        actual_data = pd.read_excel(expected_file_name)
        actual_data.query("index == 16", inplace=True)

        actual_data_str = actual_data.iloc[0].to_string(index=False)

        try:
            pd.testing.assert_frame_equal(actual_data, expected_data, check_exact=False, check_dtype=False, atol=1)
            rec.pass_case(None)
        except AssertionError as e:
            formatted = format_error_message(
            custom_message=(f"Your `{expected_file_name}` file didn't contain the expected values for index 16:\n"
                            f"### Expected excel file values:\n"
                            f"```\n{expected_data_str}\n```\n"
                            f"### Your excel file values:\n"
                            f"```\n{actual_data_str}\n```\n"
                            f"### How to fix it:\n"
                            f"You likely aren't following the instructions to change the value of the row at index 16"),
            current_test_name=current_test_name,
            input_test_case=None,
            display_inputs=False,
            )
            rec.fail_case(None, custom_message=formatted)
            
    # assert raises an AssertionError, but I don't want to actually catch it
    # this is just so I can have another Exception catch below it in case
    # anything else goes wrong.
    except AssertionError:
        raise
    
    except Exception as e:
        # Handle other exceptions
        exception_message_for_students(e, None, current_test_name)

    finally:
        # After all cases, emit a one-line summary or a short failure directing to the MD file
        pc_finalize_and_maybe_fail(rec)

            