# LocalBitcoins API

This is a fork of https://github.com/mgp25/LocalBitcoins-API.

My Purpose is to make the API fully OO-compatible allowing for users
to easily program their LocalBitcoins Bots.

In the future I plan to opensource mine, but for now only the API.

LocalBitcoins documentation: https://localbitcoins.com/api-docs/

## Examples

```python
import LocalBitcoin

lc = LocalBitcoin.LocalBitcoin(hmac_auth_key, hmac_auth_secret, False)
lc.getMyself()
```

To generate `hmac_auth_key` (key) and `hmac_auth_secret` (secret), go to: https://localbitcoins.com/accounts/api/

If you want debug enabled, change `False` to `True`

## MIT License
