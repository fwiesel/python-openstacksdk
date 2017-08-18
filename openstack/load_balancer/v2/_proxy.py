# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.load_balancer.v2 import listener as _listener
from openstack.load_balancer.v2 import load_balancer as _lb
from openstack.load_balancer.v2 import member as _member
from openstack.load_balancer.v2 import pool as _pool
from openstack import proxy2


class Proxy(proxy2.BaseProxy):

    def create_load_balancer(self, **attrs):
        """Create a new load balancer from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.load_balancer.v2.
                           load_balancer.LoadBalancer`,
                           comprised of the properties on the
                           LoadBalancer class.

        :returns: The results of load balancer creation
        :rtype: :class:`~openstack.load_balancer.v2.load_balancer.LoadBalancer`
        """
        return self._create(_lb.LoadBalancer, **attrs)

    def get_load_balancer(self, *attrs):
        """Get a load balancer

        :param load_balancer: The value can be the name of a load balancer
             or :class:`~openstack.load_balancer.v2.load_balancer.LoadBalancer`
             instance.

        :returns: One
             :class:`~openstack.load_balancer.v2.load_balancer.LoadBalancer`
        """
        return self._get(_lb.LoadBalancer, *attrs)

    def load_balancers(self, **query):
        """Retrieve a generator of load balancers

        :returns: A generator of load balancer instances
        """
        return self._list(_lb.LoadBalancer, paginated=True, **query)

    def delete_load_balancer(self, load_balancer, ignore_missing=True):
        """Delete a load balancer

        :param load_balancer: The load_balancer can be either the name or a
            :class:`~openstack.load_balancer.v2.load_balancer.LoadBalancer`
            instance
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the load balancer does not exist.
            When set to ``True``, no exception will be set when attempting to
            delete a nonexistent load balancer.

        :returns: ``None``
        """
        return self._delete(_lb.LoadBalancer, load_balancer,
                            ignore_missing=ignore_missing)

    def find_load_balancer(self, name_or_id, ignore_missing=True):
        """Find a single load balancer

        :param name_or_id: The name or ID of a load balancer
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised
            when the load balancer does not exist.
            When set to ``True``, no exception will be set when attempting
            to delete a nonexistent load balancer.

        :returns: ``None``
        """
        return self._find(_lb.LoadBalancer, name_or_id,
                          ignore_missing=ignore_missing)

    def update_load_balancer(self, load_balancer, **attrs):
        """Update a load balancer

        :param load_balancer: The load_balancer can be either the name or a
            :class:`~openstack.load_balancer.v2.load_balancer.LoadBalancer`
            instance
        :param dict attrs: The attributes to update on the load balancer
                           represented by ``load_balancer``.

        :returns: The updated load_balancer
        :rtype: :class:`~openstack.load_balancer.v2.load_balancer.LoadBalancer`
        """
        return self._update(_lb.LoadBalancer, load_balancer, **attrs)

    def create_listener(self, **attrs):
        """Create a new listener from attributes

        :param dict attrs: Keyword arguments which will be used to create a
                        :class:`~openstack.load_balancer.v2.listener.Listener`,
                        comprised of the properties on the Listener class.

        :returns: The results of listener creation
        :rtype: :class:`~openstack.load_balancer.v2.listener.Listener`
        """
        return self._create(_listener.Listener, **attrs)

    def delete_listener(self, listener, ignore_missing=True):
        """Delete a listener

        :param listener: The value can be either the ID of a listner or a
               :class:`~openstack.load_balancer.v2.listener.Listener` instance.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the listner does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent listener.

        :returns: ``None``
        """
        self._delete(_listener.Listener, listener,
                     ignore_missing=ignore_missing)

    def find_listener(self, name_or_id, ignore_missing=True):
        """Find a single listener

        :param name_or_id: The name or ID of a listener.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.

        :returns: One :class:`~openstack.load_balancer.v2.listener.Listener`
         or None
        """
        return self._find(_listener.Listener, name_or_id,
                          ignore_missing=ignore_missing)

    def get_listener(self, listener):
        """Get a single listener

        :param listener: The value can be the ID of a listener or a
               :class:`~openstack.load_balancer.v2.listener.Listener`
               instance.

        :returns: One :class:`~openstack.load_balancer.v2.listener.Listener`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        return self._get(_listener.Listener, listener)

    def listeners(self, **query):
        """Return a generator of listeners

        :param dict query: Optional query parameters to be sent to limit
                           the resources being returned. Valid parameters are:
        :returns: A generator of listener objects
        :rtype: :class:`~openstack.load_balancer.v2.listener.Listener`
        """
        return self._list(_listener.Listener, paginated=True, **query)

    def update_listener(self, listener, **attrs):
        """Update a listener

        :param listener: Either the id of a listener or a
                      :class:`~openstack.load_balancer.v2.listener.Listener`
                      instance.
        :param dict attrs: The attributes to update on the listener
                           represented by ``listener``.

        :returns: The updated listener
        :rtype: :class:`~openstack.load_balancer.v2.listener.Listener`
        """
        return self._update(_listener.Listener, listener, **attrs)

    def create_pool(self, **attrs):
        """Create a new pool from attributes

        :param dict attrs: Keyword arguments which will be used to create
                           a :class:`~openstack.load_balancer.v2.
                           pool.Pool`,
                           comprised of the properties on the
                           Pool class.

        :returns: The results of Pool creation
        :rtype: :class:`~openstack.load_balancer.v2.pool.Pool`
        """
        return self._create(_pool.Pool, **attrs)

    def get_pool(self, *attrs):
        """Get a pool

        :param pool: Value is
            :class:`~openstack.load_balancer.v2.pool.Pool`
            instance.

        :returns: One
             :class:`~openstack.load_balancer.v2.pool.Pool`
        """
        return self._get(_pool.Pool, *attrs)

    def pools(self, **query):
        """Retrieve a generator of pools

        :returns: A generator of Pool instances
        """
        return self._list(_pool.Pool, paginated=True, **query)

    def delete_pool(self, pool, ignore_missing=True):
        """Delete a pool

        :param pool: The pool is a
            :class:`~openstack.load_balancer.v2.pool.Pool`
            instance
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised when
            the pool does not exist.
            When set to ``True``, no exception will be set when attempting to
            delete a nonexistent pool.

        :returns: ``None``
        """
        return self._delete(_pool.Pool, pool,
                            ignore_missing=ignore_missing)

    def find_pool(self, name_or_id, ignore_missing=True):
        """Find a single pool

        :param name_or_id: The name or ID of a pool
        :param bool ignore_missing: When set to ``False``
            :class:`~openstack.exceptions.ResourceNotFound` will be raised
            when the pool does not exist.
            When set to ``True``, no exception will be set when attempting
            to delete a nonexistent pool.

        :returns: ``None``
        """
        return self._find(_pool.Pool, name_or_id,
                          ignore_missing=ignore_missing)

    def update_pool(self, pool, **attrs):
        """Update a pool

        :param pool: Either the id of a pool or a
                      :class:`~openstack.load_balancer.v2.pool.Pool`
                      instance.
        :param dict attrs: The attributes to update on the pool
                           represented by ``pool``.

        :returns: The updated pool
        :rtype: :class:`~openstack.load_balancer.v2.pool.Pool`
        """
        return self._update(_pool.Pool, pool, **attrs)

    def create_member(self, pool, **attrs):
        """Create a new member from attributes

        :param pool: The pool can be either the ID of a pool or a
                     :class:`~openstack.load_balancer.v2.pool.Pool` instance
                     that the member will be created in.
        :param dict attrs: Keyword arguments which will be used to create
            a :class:`~openstack.load_balancer.v2.member.Member`,
            comprised of the properties on the Member class.

        :returns: The results of member creation
        :rtype: :class:`~openstack.load_balancer.v2.member.Member`
        """
        poolobj = self._get_resource(_pool.Pool, pool)
        return self._create(_member.Member, pool_id=poolobj.id,
                            **attrs)

    def delete_member(self, member, pool, ignore_missing=True):
        """Delete a member

        :param member:
            The member can be either the ID of a member or a
            :class:`~openstack.load_balancer.v2.member.Member` instance.
        :param pool: The pool can be either the ID of a pool or a
                     :class:`~openstack.load_balancer.v2.pool.Pool` instance
                     that the member belongs to.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the member does not exist.
                    When set to ``True``, no exception will be set when
                    attempting to delete a nonexistent member.

        :returns: ``None``
        """
        poolobj = self._get_resource(_pool.Pool, pool)
        self._delete(_member.Member, member,
                     ignore_missing=ignore_missing, pool_id=poolobj.id)

    def find_member(self, name_or_id, pool, ignore_missing=True):
        """Find a single member

        :param str name_or_id: The name or ID of a member.
        :param pool: The pool can be either the ID of a pool or a
                     :class:`~openstack.load_balancer.v2.pool.Pool` instance
                     that the member belongs to.
        :param bool ignore_missing: When set to ``False``
                    :class:`~openstack.exceptions.ResourceNotFound` will be
                    raised when the resource does not exist.
                    When set to ``True``, None will be returned when
                    attempting to find a nonexistent resource.

        :returns: One :class:`~openstack.load_balancer.v2.member.Member`
                  or None
        """
        poolobj = self._get_resource(_pool.Pool, pool)
        return self._find(_member.Member, name_or_id,
                          ignore_missing=ignore_missing, pool_id=poolobj.id)

    def get_member(self, member, pool):
        """Get a single member

        :param member: The member can be the ID of a member or a
                       :class:`~openstack.load_balancer.v2.member.Member`
                       instance.
        :param pool: The pool can be either the ID of a pool or a
                     :class:`~openstack.load_balancer.v2.pool.Pool` instance
                     that the member belongs to.

        :returns: One :class:`~openstack.load_balancer.v2.member.Member`
        :raises: :class:`~openstack.exceptions.ResourceNotFound`
                 when no resource can be found.
        """
        poolobj = self._get_resource(_pool.Pool, pool)
        return self._get(_member.Member, member,
                         pool_id=poolobj.id)

    def members(self, pool, **query):
        """Return a generator of members

        :param pool: The pool can be either the ID of a pool or a
                     :class:`~openstack.load_balancer.v2.pool.Pool` instance
                     that the member belongs to.
        :param dict query: Optional query parameters to be sent to limit
                           the resources being returned. Valid parameters are:

        :returns: A generator of member objects
        :rtype: :class:`~openstack.load_balancer.v2.member.Member`
        """
        poolobj = self._get_resource(_pool.Pool, pool)
        return self._list(_member.Member, paginated=True,
                          pool_id=poolobj.id, **query)

    def update_member(self, member, pool, **attrs):
        """Update a member

        :param member: Either the ID of a member or a
                       :class:`~openstack.load_balancer.v2.member.Member`
                       instance.
        :param pool: The pool can be either the ID of a pool or a
                     :class:`~openstack.load_balancer.v2.pool.Pool` instance
                     that the member belongs to.
        :param dict attrs: The attributes to update on the member
                           represented by ``member``.

        :returns: The updated member
        :rtype: :class:`~openstack.load_balancer.v2.member.Member`
        """
        poolobj = self._get_resource(_pool.Pool, pool)
        return self._update(_member.Member, member,
                            pool_id=poolobj.id, **attrs)