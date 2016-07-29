#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import vobject

vo = vobject.vCard()

vo.add('version')
vo.version.value="3.0"

vo.add('n')
vo.n.value = vobject.vcard.Name(family="Völgyes", given = "David")
vo.add('fn')
vo.fn.value = "David Völgyes"

vo.add('email')
vo.email.value="david.volgyes@ntnu.no"
vo.email.type_param='INTERNET'

vo.add('tel')
vo.tel.type_param = "cell"
vo.tel.value = "+47 4717 0724"

vo.add('source')
#https://git.io/vo08t
vo.source.value = 'https://git.io/vo08t'
#vo.source.value = 'https://raw.githubusercontent.com/dvolgyes/personal/master/vcard/ntnu.vcf'

with open('../ntnu_simplified.vcf','wt') as f:
    f.write(vo.serialize())

vo.add('title')
vo.title.value = 'PhD fellow'

vo.add('key')
vo.key.type_param='PGP'
vo.key.value="https://raw.githubusercontent.com/dvolgyes/personal/master/pgp/ntnu.asc"

vo.add('url')
vo.url.value = "https://no.linkedin.com/in/davidvolgyes"

#vo.add('url')
#vo.url.value = "http://orcid.org/0000-0001-9723-5532"

vo.add('org')
vo.org.value = ["Faculty of Computer Science and Media Technology","Norwegian University of Science and Technology"]

with open('../ntnu.vcf','wt') as f:
    f.write(vo.serialize())
