-- Swamp Bike Opera embedded system for Kaffe Matthews 
-- Copyright (C) 2012 Wolfgang Hauptfleisch, Dave Griffiths
--
-- This program is free software: you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with this program.  If not, see <http://www.gnu.org/licenses/>.

require ('osc.client')
require 'utils'

module("send_osc", package.seeall)

local osc = osc.client.new{host = '127.0.0.1', port = 8888}

-- osc version
function send_events(events,pos_state)
    -- now look through all the maps for new events
    for k,layer in pairs(events) do       
        for k,event in pairs(layer) do
	    print("sending...")
	    osc:send({'#bundle',os.time(),
		{"/"..event.type,
		"s",event.zone_name,
		}})
	    print("sent...")
	end
    end
end
