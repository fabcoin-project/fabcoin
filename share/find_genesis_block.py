#!/usr/bin/env python

from hashlib import sha256

VERSION    = '01000000'.decode('hex')
PREVBLOCK  = '00'.decode('hex') * 32
MERKLEROOT = 'bdc8f49a91a4535a15f76b486cc9fe0d70bdaa8812f58ce80ba41e97aa1b3bf5'.decode('hex')
DIFFICULTY = 'ffff001d'.decode('hex')

def block_hash(unixtime, nonce):
  unixtime = hex(unixtime)[2:].decode('hex')[::-1]
  nonce    = hex(nonce)[2:]
  nonce    = '0'*(8-len(nonce)) + nonce
  nonce    = nonce.decode('hex')[::-1]
  return sha256(sha256(
      VERSION + PREVBLOCK + MERKLEROOT + unixtime + DIFFICULTY + nonce
    ).digest()).digest()

unixtime = 1356123600
nonce    = 0
print "Starting at unixtime %d and nonce %d" % (unixtime, nonce)
while block_hash(unixtime, nonce)[-4:] != '\x00\x00\x00\x00':
  nonce = nonce+1
  if nonce > 4294967295:
    unixtime, nonce = unixtime+1, 0
    print "Advancing to unixtime %d and nonce %d" % (unixtime, nonce)
  elif 0 == (nonce%100000):
    print nonce

print 'Found block!'
print "UNIXTIME: %d" % unixtime
print "NONCE:    %d" % nonce
print "HASH:     %s" % block_hash(unixtime, nonce)[::-1].encode('hex')
