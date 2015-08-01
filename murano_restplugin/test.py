from murano_restplugin import REST

if __name__ == "__main__":
    rest = REST()
    rest.initialize(_context=None, base_url='http://httpbin.org')
    print rest.makeRequest('/ip', parse_json=False)
