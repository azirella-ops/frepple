#!/usr/bin/python

#
# Copyright (C) 2007-2012 by Johan De Taeye, frePPLe bvba
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

#  file     : $URL$
#  revision : $LastChangedRevision$  $LastChangedBy$
#  date     : $LastChangedDate$

import frepple
import os



try:
  print "Initializing:"
  frepple.FreppleInitialize()
  print " OK"
  print "Reading base data:"
  frepple.FreppleReadXMLData('<?xml version="1.0" encoding="UTF-8" ?> \
    <plan xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"> \
      <name>actual plan</name> \
      <description>anything goes</description> \
      <current>2007-01-01T00:00:01</current> \
      <operations> \
        <operation name="make end item" xsi:type="operation_fixed_time"> \
          <duration>P1D</duration> \
        </operation> \
      </operations> \
      <items> \
        <item name="end item"> \
          <operation name="delivery end item" xsi:type="operation_fixed_time"> \
            <duration>P1D</duration> \
          </operation> \
        </item> \
      </items> \
      <buffers> \
        <buffer name="end item"> \
          <producing name="make end item"/> \
          <item name="end item"/> \
        </buffer> \
      </buffers> \
      <resources> \
        <resource name="resource"> \
          <maximum name="capacity" xsi:type="calendar_double"> \
            <buckets> \
              <bucket start="2007-01-01T00:00:01" value="1"/> \
            </buckets> \
          </maximum> \
          <loads> \
            <load> \
              <operation name="make end item" /> \
            </load> \
          </loads> \
        </resource> \
      </resources> \
      <flows> \
        <flow xsi:type="flow_start"> \
          <operation name="delivery end item"/> \
          <buffer name="end item"/> \
          <quantity>-1</quantity> \
        </flow> \
        <flow xsi:type="flow_end"> \
          <operation name="make end item"/> \
          <buffer name="end item"/> \
          <quantity>1</quantity> \
        </flow> \
      </flows> \
      <demands> \
        <demand name="order 1"> \
          <quantity>10</quantity> \
          <due>2007-01-04T09:00:00</due> \
          <priority>1</priority> \
          <item name="end item"/> \
        </demand> \
      </demands> \
    </plan> ', True, False)
  print " OK"

  print "Adding an item:"
  frepple.FreppleReadXMLData('<?xml version="1.0" encoding="UTF-8" ?> \
    <plan xmlns:xsi="http://www.w3.org/2001/xmlschema-instance"> \
      <items> \
        <item name="new item"/> \
      </items> \
    </plan>', 1, 0)
  print " OK"

  print "Saving frepple model to a file:"
  frepple.FreppleSaveFile("turbo.python.xml")
  print " OK"

  print "Passing invalid XML data to frepple:"
  frepple.FreppleReadXMLData('<?xml version="1.0" encoding="UTF-8" ?> \
    <plan xmlns:xsi="http://www.w3.org/2001/xmlschema-instance"> \
      <xxdescription>dummy</xxdescription> \
    </plan> ', 1, 0)
  print " OK"

  print "End of frepple commands"
except RuntimeError as inst:
  print "Runtime exception caught: " + str(inst)
except:
  print "Caught an unknown exception"
else:
  print "All commands passed without error"

print "Exiting..."
