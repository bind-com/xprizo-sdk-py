# coding: utf-8

"""
    Xprizo API

    Xprizo api endpoints  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@xprizo.com
    Generated by: https://openapi-generator.tech
"""

from xprizo_sdk_py.paths.api_task_add_attachment_id.post import ApiTaskAddAttachmentIdPost
from xprizo_sdk_py.paths.api_task_add_comment_id.post import ApiTaskAddCommentIdPost
from xprizo_sdk_py.paths.api_task_cancel_id.put import ApiTaskCancelIdPut
from xprizo_sdk_py.paths.api_task_daily_withdrawal_limit_request_account_id.post import ApiTaskDailyWithdrawalLimitRequestAccountIdPost
from xprizo_sdk_py.paths.api_task_get_id.get import ApiTaskGetIdGet
from xprizo_sdk_py.paths.api_task_hide_id.put import ApiTaskHideIdPut
from xprizo_sdk_py.paths.api_task_one_off_withdrawal_amount_request_account_id.post import ApiTaskOneOffWithdrawalAmountRequestAccountIdPost
from xprizo_sdk_py.paths.api_task_show_id.put import ApiTaskShowIdPut


class TaskApi(
    ApiTaskAddAttachmentIdPost,
    ApiTaskAddCommentIdPost,
    ApiTaskCancelIdPut,
    ApiTaskDailyWithdrawalLimitRequestAccountIdPost,
    ApiTaskGetIdGet,
    ApiTaskHideIdPut,
    ApiTaskOneOffWithdrawalAmountRequestAccountIdPost,
    ApiTaskShowIdPut,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
