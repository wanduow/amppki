# This file is part of amppki.
#
# Copyright (C) 2015-2019 The University of Waikato, Hamilton, New Zealand.
#
# Authors: Brendon Jones
#
# All rights reserved.
#
# This code has been developed by the WAND Network Research Group at the
# University of Waikato. For further information please see
# http://www.wand.net.nz/
#
# amppki is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# amppki is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with amppki; if not, write to the Free Software Foundation, Inc.
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# Please report any bugs, questions or comments to contact@wand.net.nz
#

""" Global config options that are used by both the web and cli scripts """

CA_DIR = "/etc/amppki"
CERT_DIR = "%s/certs" % CA_DIR
CSR_DIR = "%s/csr" % CA_DIR
RABBITMQCTL = "/usr/sbin/rabbitmqctl"

INDEX_FILE = "%s/index.txt" % CA_DIR
