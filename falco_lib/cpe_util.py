#!/usr/bin/env python
""" utility for cpe comparison

"""
import cpe
# from pkg_resources import parse_version


def cpe_clip(version, cpe_list_str):
    """
        CPE matches returned have long lists of CPEs.  While that's
        interesting to see what all is vulnerable, you might want to just
        want to see from the version you are matching to the last vulnerable
        version, what is vulnerable.

        requires: cpe library, distutils version comparison functions

            inputs: version string, cpe_list
            output: shortened CPE list, all the versions previous to the
            version supplied are trimmed out.

    """
    cpe_list = cpe_list_str.split(',')
    cpe_list.sort()
    cpe_list_out = []
    for cpe_data in cpe_list:
        cpe_item = cpe.CPE(cpe_data)
        if cpe_item.get_attribute_values('version')[0] >= version:
                cpe_list_out.append(cpe_data)
    cpe_string_out = ','.join(cpe_list_out)
    return cpe_string_out


def main():
    """ testing
    """
    cpes = [u'cpe:/a:openssl:openssl:1.0.1s', u'cpe:/a:openssl:openssl:1.0.2', u'cpe:/a:openssl:openssl:1.0.2:beta1', u'cpe:/a:openssl:openssl:1.0.2:beta2', u'cpe:/a:openssl:openssl:1.0.2:beta3', u'cpe:/a:openssl:openssl:1.0.2a', u'cpe:/a:openssl:openssl:1.0.2b', u'cpe:/a:openssl:openssl:1.0.2c', u'cpe:/a:openssl:openssl:1.0.2d', u'cpe:/a:openssl:openssl:1.0.2e', u'cpe:/a:openssl:openssl:1.0.2f', u'cpe:/a:openssl:openssl:1.0.2g']
    version = '1.0.2a'
    cpes_string = ','.join(cpes)
    for each in cpes:
        version = each.split(':')[4]
        print "Version: %s\nClipped CPEs: %s" % (version, cpe_clip(version, cpes_string))


if __name__ == "__main__":
    main()
