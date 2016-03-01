import yaml


class ConfigManager:

    def __init__(self):
        config_file = 'resources/config.yaml'
        config_raw = open(config_file).read()
        self.config = yaml.load(config_raw)
        self.git_user = self.config['Credentials']['Github']['User']
        self.git_pass = self.config['Credentials']['Github']['Password']
        self.ldap_user = self.config['Credentials']['LDAP']['User']
        self.ldap_pass = self.config['Credentials']['LDAP']['Password']
        self.base_dn = self.config['LDAP_Settings']['Base_DN']
        self.repo_name = self.config['Git_Repo']['Repo_Name']
        self.repo_owner = self.config['Git_Repo']['Repo_Owner']
        base_url = "https://api.github.com/repos/{0}/{1}/issues"
        self.issues_url = base_url.format(self.repo_owner, self.repo_name)
