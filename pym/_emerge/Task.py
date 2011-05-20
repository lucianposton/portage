# Copyright 1999-2011 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2

from _emerge.SlotObject import SlotObject
class Task(SlotObject):
	__slots__ = ("_hash_key", "_hash_value")

	def __eq__(self, other):
		try:
			return self._hash_key == other._hash_key
		except AttributeError:
			return False

	def __ne__(self, other):
		try:
			return self._hash_key != other._hash_key
		except AttributeError:
			return True

	def __hash__(self):
		return self._hash_value

	def __len__(self):
		return len(self._hash_key)

	def __getitem__(self, key):
		return self._hash_key[key]

	def __iter__(self):
		return iter(self._hash_key)

	def __contains__(self, key):
		return key in self._hash_key

	def __str__(self):
		"""
		Emulate tuple.__repr__, but don't show 'foo' as u'foo' for unicode
		strings.
		"""
		return "(%s)" % ", ".join(("'%s'" % x for x in self._hash_key))
