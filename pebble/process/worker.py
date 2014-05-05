# This file is part of Pebble.

# Pebble is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation,
# either version 3 of the License, or (at your option) any later version.

# Pebble is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with Pebble.  If not, see <http://www.gnu.org/licenses/>.


from functools import wraps
from multiprocessing import Process


def worker(daemon=False):
    """Runs the decorated *function* in a separate process.

    Returns the *Process* object.

    """
    def wrap(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            process = Process(target=function, args=args, kwargs=kwargs)
            process.daemon = daemon
            process.start()

            return process

        return wrapper

    return wrap
