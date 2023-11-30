from apps.core.utils import send_sms


class NotificationUser:

    @classmethod
    def handler_password_changed_successfully(cls, notification, phonenumber):
        pattern = 'iseiyg8otwl06bi'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_reset_password_code_sent(cls, notification, phonenumber):
        pattern = 'xka1tvkiqiwnrjx'
        send_sms(phonenumber, pattern, {
            'code': notification.kwargs['code']
        })

    @classmethod
    def handler_diet_program_add(cls, notification, phonenumber):
        pattern = '256coltlz20rhdk'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })

    @classmethod
    def handler_training_program_add(cls, notification, phonenumber):
        pattern = '2l60364z6y8fs06'
        send_sms(phonenumber, pattern, {
            'user_name': notification.to_user.get_full_name()
        })


NOTIFICATION_USER_HANDLERS = {
    'PASSWORD_CHANGED_SUCCESSFULLY': NotificationUser.handler_password_changed_successfully,
    'RESET_PASSWORD_CODE_SENT': NotificationUser.handler_reset_password_code_sent,
    'DIET_PROGRAM_ADD': NotificationUser.handler_diet_program_add,
    'TRAINING_PROGRAM_ADD': NotificationUser.handler_training_program_add,
}
