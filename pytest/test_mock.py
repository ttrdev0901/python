import os
from db_access import selectById



# def get_record(filepath: str):
#     """[summary]

#     Args:
#         filepath ([type]): [description]

#     Returns:
#         [type]: [description]
#     """
#     try:
#         if not os.path.isfile(filepath):
#             return 'filepath is not found'

#         os.remove(filepath)
#         return 'file is deleted'

#     except Exception:
#         return 'error is occured'


# def test_file_not_exist(mocker):

#     mocker.patch('os.path.isfile', return_value=False)

#     message = delete_file('test_file_path')

#     assert message == 'filepath is not found'
