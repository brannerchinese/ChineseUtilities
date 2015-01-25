// +---------------------------------------------------------------------------+
// | Media Gallery Plugin 1.6                                                  |
// +---------------------------------------------------------------------------+
// | $Id:: rating.js 2349 2008-06-03 00:00:30Z mevans0263                     $|
// | Javascript (MooTools v1.11 based) to handle AJAX rating sub-system        |
// +---------------------------------------------------------------------------+
// | Copyright (C) 2005-2008 by the following authors:                         |
// |                                                                           |
// | Mark R. Evans              - mark@gllabs.org                              |
// +---------------------------------------------------------------------------+
// | Based on work by:                                                         |
// | Ryan Masuga, masugadesign.com  - ryan@masugadesign.com                    |
// | Masuga Design                                                             |
// |(http://masugadesign.com/the-lab/scripts/unobtrusive-ajax-star-rating-bar/)|
// | Komodo Media (http://komodomedia.com)                                     |
// | Climax Designs (http://slim.climaxdesigns.com/)                           |
// +---------------------------------------------------------------------------+
// |                                                                           |
// | This program is free software; you can redistribute it and/or             |
// | modify it under the terms of the GNU General Public License               |
// | as published by the Free Software Foundation; either version 2            |
// | of the License, or (at your option) any later version.                    |
// |                                                                           |
// | This program is distributed in the hope that it will be useful,           |
// | but WITHOUT ANY WARRANTY; without even the implied warranty of            |
// | MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             |
// | GNU General Public License for more details.                              |
// |                                                                           |
// | You should have received a copy of the GNU General Public License         |
// | along with this program; if not, write to the Free Software Foundation,   |
// | Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.           |
// |                                                                           |
// +---------------------------------------------------------------------------+
//

window.addEvent('load',function() {
    $$('.rater').addEvent('click',function(e) {
        e = new Event(e).stop();

		var parameterString = this.href.replace(/.*\?(.*)/, "$1"); // onclick="sndReq('j=1&q=2&t=127.0.0.1&c=5');
		var parameterTokens = parameterString.split("&"); // onclick="sndReq('j=1,q=2,t=127.0.0.1,c=5');
		var parameterList = new Array();

		for (j = 0; j < parameterTokens.length; j++) {
			var parameterName = parameterTokens[j].replace(/(.*)=.*/, "$1"); // j
			var parameterValue = parameterTokens[j].replace(/.*=(.*)/, "$1"); // 1
			parameterList[parameterName] = parameterValue;
		}
		var theratingID = parameterList['id'];
		var theVote     = parameterList['score'];
		var theuserIP   = parameterList['t'];
		var theunits    = parameterList['c'];
		var thesize     = parameterList['s'];
		var thedivID     = parameterList['d'];
		var theshowTotals     = parameterList['st'];

        new Ajax('/rating/rater_rpc.php?score='+theVote+'&id='+theratingID+'&t='+theuserIP+'&c='+theunits+'&s='+thesize+'&d='+thedivID+'&st='+theshowTotals,
            {
                method: 'get',
                data: this,
                evalScripts: true,
                update: $('unit_long'+thedivID)
            }).request();
        return false;
    });
});