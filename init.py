################################################################################
# Initializes the database for user login/storage                              #
#                                                                              #
# Authors                                                                      #
#  Yicheng Wang                                                                #
#                                                                              #
# Description                                                                  #
#  Initializes database in db/ for user login and storage                      #
#                                                                              #
################################################################################

# TODO
#  create tables

# Dev Log
#  Project Created: 2015-12-19 12:42 - Yicheng W.

import sqlite3
from hashlib import sha256
from database import *

conn = sqlite3.connect("./db/infos.db")

c = conn.cursor()

create_base = "CREATE TABLE %s (%s)" # no user input needed, use %s

 # password = hexstring of hash
c.execute(create_base % ("users", "email TEXT, password TEXT, first TEXT, last TEXT"))

# note will be html source code with markup
c.execute(create_base % ("sites", "id INTEGER, email TEXT, title TEXT, site TEXT, comments TEXT, notes TEXT, shared INTEGER, t INTEGER"))

conn.commit()

m = sha256()
m.update("12345")
hash = m.hexdigest()

q = """INSERT INTO users VALUES (?, ?, ?, ?)"""

c.execute(q, ('alex.wyc2098@gmail.com', hash, 'Yicheng', 'Wang'))

conn.commit()

site = """
        <h1>Lorem ipsum</h1>

	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ex diam, lobortis ut euismod ac, congue at lacus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. <span class="comment">Maecenas aliquet mauris elit, id tristique est rhoncus quis. Nullam vel dolor sit amet lorem ultrices feugiat. In vitae ultrices odio, et venenatis nibh.</span> <span class="comment">Praesent</span> dignissim ornare ornare. Pellentesque tempus at elit a gravida. Maecenas non gravida neque. Suspendisse tristique mi id massa malesuada, nec malesuada velit iaculis. Fusce massa magna, elementum id tortor et, elementum blandit magna. Ut sed risus sem. Praesent ex diam, dapibus a mi sed, luctus dignissim enim.</p>

	<p>Suspendisse bibendum est pharetra ligula ullamcorper, nec ultricies urna pellentesque. Nunc in laoreet elit, a tincidunt tellus. In hac habitasse platea dictumst. Nullam augue eros, tristique eu accumsan in, molestie sed urna. In auctor nec quam ut volutpat. Mauris vitae massa at ante placerat ornare. Nunc dapibus dignissim ligula. <span class="comment">Lorem ipsum</span> dolor sit amet, consectetur adipiscing elit. Proin in lectus vel urna semper pellentesque. Aliquam diam sapien, suscipit non accumsan sit amet, consequat nec leo. Morbi placerat malesuada massa ac hendrerit. Vestibulum id tristique tortor. Fusce tristique ipsum sed lectus commodo tincidunt. Nullam hendrerit mi enim, at lobortis tortor faucibus non.</p>

	<p>Aliquam ut velit mi. Cras hendrerit efficitur purus. Nullam ut sapien cursus, pellentesque eros sed, faucibus enim. Curabitur arcu quam, blandit vel orci ac, ultricies pharetra quam. <span class="comment">Suspendisse sed venenatis nibh, vitae consequat metus. Integer pellentesque sit amet sem sed congue. Fusce venenatis sagittis eros, id viverra est tempus at. Nullam dictum massa enim. Nulla interdum egestas dignissim. Fusce nec dolor luctus, facilisis erat sit amet, varius dolor. Morbi mollis at lorem quis sollicitudin.</span></p>

	<p>Nam ornare ac ipsum ac aliquet. Pellentesque et turpis semper, cursus purus nec, congue tortor. Quisque varius eros in nisl aliquam aliquet. Vivamus auctor cursus sapien, id pulvinar diam auctor eu. Curabitur blandit mollis dolor nec scelerisque. <span class="comment">Quisque</span> eu pulvinar est. Pellentesque vel eros purus. Cras id leo non turpis rhoncus elementum. Mauris condimentum dolor nisi, nec venenatis magna venenatis sed. Sed ultrices nunc enim, ut laoreet sem aliquam sed. Aliquam id sapien sem. Ut a purus at ligula commodo suscipit sed accumsan urna. Curabitur eu consequat erat. Praesent a massa ac nunc faucibus elementum. Maecenas eu venenatis arcu. Phasellus mattis a est at <span class="comment">pellent</span>esque.</p>

	<p>Aenean eget nibh sit amet nulla ultricies tempor. Etiam id magna mauris. In fringilla, ligula eu venenatis euismod, magna tellus elementum dolor, et pulvinar lorem nisl eget eros. Aenean scelerisque sapien ac diam semper vulputate ac et nibh. <span class="comment">Praesent quis ante et tellus porttitor porta id quis nunc.</span> Proin sollicitudin bibendum tempus. Fusce elit nibh, commodo a lobortis ut, eleifend a elit. Pellentesque maximus nibh nunc, quis tristique mauris egestas quis. Ut massa ex, aliquet at viverra non, porta at libero. Aliquam rhoncus scelerisque dui id molestie. Vestibulum hendrerit venenatis malesuada. Vivamus id fringilla tellus, scelerisque finibus dolor. Aenean sem nunc, sollicitudin nec lorem quis, laoreet varius tortor.</p>

"""

comment = """
<div class='comment-block white-text darken-3 black card-panel hoverable'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ex diam, lobortis ut euismod ac, congue at lacus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
<div class='comment-block white-text darken-3 black card-panel hoverable'>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque ex diam, lobortis ut euismod ac, congue at lacus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.</div>
<div class='comment-block white-text darken-3 black card-panel hoverable'>Aliquam ut velit mi.</div>
<div class='comment-block white-text darken-3 black card-panel hoverable'>Aliquam diam sapien, suscipit non accumsan sit amet, consequat nec leo. Morbi placerat malesuada massa ac hendrerit. Vestibulum id tristique tortor. Fusce tristique ipsum sed lectus commodo tincidunt. Nullam hendrerit mi enim, at lobortis tortor faucibus non.</div>
<div class='comment-block white-text darken-3 black card-panel hoverable'>Fusce nec dolor luctus, facilisis erat sit amet, varius dolor. Morbi mollis at lorem quis sollicitudin.</div>
<div class='comment-block white-text darken-3 black card-panel hoverable'>Vivamus id fringilla tellus, scelerisque finibus dolor.</div>
<div class='comment-block white-text darken-3 black card-panel hoverable'>Sed ultrices nunc enim, ut laoreet sem aliquam sed.</div>
<div class='comment-block white-text darken-3 black card-panel hoverable'>Vestibulum hendrerit venenatis malesuada.</div>

"""

add_to_sites("alex.wyc2098@gmail.com", "testing", site, comment, "");
