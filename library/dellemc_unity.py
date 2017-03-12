#!/usr/bin/python


from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(default='sync', choices=['sync', 'manual'], type='str'),
            # The following options are specific if sync is the state
            ntp_server=dict(deafult=None, type='list'),
            force=dict(default='no', type='bool'),
            # The following option is specific if manual is the state
            date_time=dict(default=None, type='str'),
            unity_username=dict(default=None, required=True, type='str'),
            unity_password=dict(default=None, required=True, type='str',
                                no_log=True),
            unity_hostname=dict(default=None, required=True, type='str'),
        )
    )
    module.exit_json(changed=False, meta=module.params)


if __name__ == '__main__':
    main()
