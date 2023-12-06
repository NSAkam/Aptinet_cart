#!/usr/bin/python

from smartcard.scard import *

##

hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_SYSTEM)

if hresult != SCARD_S_SUCCESS:
  raise error, 'SCardEstablishContext(): ' + SCardGetErrorMessage(hresult)

##

hrest, readers = SCardListReaders(hcontext, [])

if hresult != SCARD_S_SUCCESS:
  raise error, 'SCardListReaders(): ' + SCardGetErrorMessage(hresult)

##

hresult, hcard, dwActiveProtocol = SCardConnect(hcontext, readers[0], SCARD_SHARE_DIRECT, 0)

if hresult != SCARD_S_SUCCESS:
  raise error, 'SCardConnect(): ' + SCardGetErrorMessage(hresult)

##

hresult, response = SCardControl(hcard, SCARD_CTL_CODE(3500), [0xE0, 0x0, 0x0, 0x28, 0x1, 0xFF])

if hresult != SCARD_S_SUCCESS:
  raise error, 'SCardControl(): ' + SCardGetErrorMessage(hresult)

print ''.join('{:02X} '.format(x) for x in response)

##

hresult = SCardDisconnect(hcard, SCARD_LEAVE_CARD)

if hresult != SCARD_S_SUCCESS:
  raise error, 'SCardDisconnect(): ' + SCardGetErrorMessage(hresult)

##

hresult = SCardReleaseContext(hcontext)

if hresult != SCARD_S_SUCCESS:
  raise error, 'SCardReaseContext(): ' + SCardGetErrorMessage(hresult)