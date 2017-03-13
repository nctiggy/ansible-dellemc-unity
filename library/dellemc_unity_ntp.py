#!/usr/bin/python


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import open_url


class Unity(object):

    def __init__(self, module):
        self.module = module
        self.state = module.params['state']
        self.force = module.params['force']
        self.ntp_server = module.params['ntp_server']
        self.date_time = module.params['date_time']
        self.unity_hostname = module.params['unity_hostname']
        self.unity_username = module.params['unity_username']
        self.unity_password = module.params['unity_password']
        self.base_url = "https://" + self.unity_hostname + "/api"
        self.headers = {'X-EMC-REST-CLIENT': 'true',
                        'content-type': 'application/json',
                        'Accept': 'application/json'}

    def __doPost(self, url, args):
        r = open_url(url, data=args, headers=self.headers, method="POST",
                     validate_certs=False)
        return r.status_code, r.text

    def __doGet(self, url):
        r = open_url(url, method="GET", url_username=self.unity_username,
                     url_password=self.unity_password, headers=self.headers,
                     validate_certs=False)
        return r.status_code, r.text

    def start(self):
        url = self.base_url + "/instances/system/0"
        r = self.__doGet(url)
        # self.headers['EMC-CSRF-TOKEN']=r.headers['EMC-CSRF-TOKEN']
        return r


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

    unity = Unity(module)
    result = unity.start
    module.exit_json(changed=True, msg=result)


if __name__ == '__main__':
    main()
