import json
'''
Class to manipulate a Localbitcoin Ad

If you change any str attribute, don't forget to unicode it:
unicode(str). Otherwise MAC authentication fails.

'''
class LocalBitcoinAd:

 '''
 Default Empty Constructor
 ''' 
 def __init__(self):
   self._actions_change_form = ''
   self._actions_html_form = ''
   self._actions_public_view = ''
   self._account_info = ''
   self._ad_id = ''
   self._age_days_coefficient_limit = ''
   self._atm_model = ''
   self._bank_name = ''
   self._city = ''
   self._countrycode = ''
   self._created_at = ''
   self._currency = ''
   self._email = ''
   self._first_time_limit_btc = ''
   self._hidden_by_opening_hours = ''
   self._is_local_office = ''
   self._is_low_risk = ''
   self._lat = ''
   self._location_string = ''
   self._lon = ''
   self._max_amount = ''
   self._max_amount_available = ''
   self._min_amount = ''
   self._msg = ''
   self._online_provider = ''
   self._opening_hours = ''
   self._payment_window_minutes = ''
   self._price_equation = ''
   self._profile = ''
   self._require_feedback_score = ''
   self._require_identification = ''
   self._require_trade_volume = ''
   self._require_trusted_by_advertiser = ''
   self._sms_verification_required = ''
   self._temp_price = ''
   self._temp_price_usd = ''
   self._track_max_amount = ''
   self._trade_type = ''
   self._trusted_required = ''
   self._visible = ''
   self._volume_coefficient_btc = ''
 
 '''
 Contructor that takes one ad from the adlist in my_ads()
 It put everything in place. If something do not come we leave empty
 '''
 def __init__(self, ad):
  if ad['actions'].has_key('change_form') :
   self._actions_change_form= ad['actions']['change_form'] 
  else:
   self._actions_change_form = ''

  if ad['actions'].has_key('html_form') :
   self._actions_html_form= ad['actions']['html_form'] 
  else:
   self._actions_html_form = ''

  if ad['actions'].has_key('public_view') :
   self._actions_public_view= ad['actions']['public_view'] 
  else:
   self._actions_public_view = ''

  if ad['data'].has_key('account_info') :
   self._account_info= ad['data']['account_info'] 
  else:
   self._account_info = ''

  if ad['data'].has_key('ad_id') :
   self._ad_id= ad['data']['ad_id'] 
  else:
   self._ad_id = ''

  if ad['data'].has_key('age_days_coefficient_limit') :
   self._age_days_coefficient_limit= ad['data']['age_days_coefficient_limit'] 
  else:
   self._age_days_coefficient_limit = ''

  if ad['data'].has_key('atm_model') :
   self._atm_model= ad['data']['atm_model'] 
  else:
   self._atm_model = ''

  if ad['data'].has_key('bank_name') :
   self._bank_name= ad['data']['bank_name'] 
  else:
   self._bank_name = ''

  if ad['data'].has_key('city') :
   self._city= ad['data']['city'] 
  else:
   self._city = ''

  if ad['data'].has_key('countrycode') :
   self._countrycode= ad['data']['countrycode'] 
  else:
   self._countrycode = ''

  if ad['data'].has_key('created_at') :
   self._created_at= ad['data']['created_at'] 
  else:
   self._created_at = ''

  if ad['data'].has_key('currency') :
   self._currency= ad['data']['currency'] 
  else:
   self._currency = ''

  if ad['data'].has_key('email') :
   self._email= ad['data']['email'] 
  else:
   self._email = ''

  if ad['data'].has_key('first_time_limit_btc') :
   self._first_time_limit_btc= ad['data']['first_time_limit_btc'] 
  else:
   self._first_time_limit_btc = ''

  if ad['data'].has_key('hidden_by_opening_hours') :
   self._hidden_by_opening_hours= ad['data']['hidden_by_opening_hours'] 
  else:
   self._hidden_by_opening_hours = ''

  if ad['data'].has_key('is_local_office') :
   self._is_local_office= ad['data']['is_local_office'] 
  else:
   self._is_local_office = ''

  if ad['data'].has_key('is_low_risk') :
   self._is_low_risk= ad['data']['is_low_risk'] 
  else:
   self._is_low_risk = ''

  if ad['data'].has_key('lat') :
   self._lat= ad['data']['lat'] 
  else:
   self._lat = ''

  if ad['data'].has_key('location_string') :
   self._location_string= ad['data']['location_string'] 
  else:
   self._location_string = ''

  if ad['data'].has_key('lon') :
   self._lon= ad['data']['lon'] 
  else:
   self._lon = ''

  if ad['data'].has_key('max_amount') :
   self._max_amount= ad['data']['max_amount'] 
  else:
   self._max_amount = ''

  if ad['data'].has_key('max_amount_available') :
   self._max_amount_available= ad['data']['max_amount_available'] 
  else:
   self._max_amount_available = ''

  if ad['data'].has_key('min_amount') :
   self._min_amount= ad['data']['min_amount'] 
  else:
   self._min_amount = ''

  if ad['data'].has_key('msg') :
   self._msg= ad['data']['msg'] 
  else:
   self._msg = ''

  if ad['data'].has_key('online_provider') :
   self._online_provider= ad['data']['online_provider'] 
  else:
   self._online_provider = ''

  if ad['data'].has_key('opening_hours') :
   self._opening_hours= ad['data']['opening_hours'] 
  else:
   self._opening_hours = ''

  if ad['data'].has_key('payment_window_minutes') :
   self._payment_window_minutes= ad['data']['payment_window_minutes'] 
  else:
   self._payment_window_minutes = ''

  if ad['data'].has_key('price_equation') :
   self._price_equation= ad['data']['price_equation'] 
  else:
   self._price_equation = ''

  if ad['data'].has_key('profile') :
   self._profile= ad['data']['profile'] 
  else:
   self._profile = ''

  if ad['data'].has_key('require_feedback_score') :
   self._require_feedback_score= ad['data']['require_feedback_score'] 
  else:
   self._require_feedback_score = ''

  if ad['data'].has_key('require_identification') :
   self._require_identification= ad['data']['require_identification'] 
  else:
   self._require_identification = ''

  if ad['data'].has_key('require_trade_volume') :
   self._require_trade_volume= ad['data']['require_trade_volume'] 
  else:
   self._require_trade_volume = ''

  if ad['data'].has_key('require_trusted_by_advertiser') :
   self._require_trusted_by_advertiser= ad['data']['require_trusted_by_advertiser'] 
  else:
   self._require_trusted_by_advertiser = ''

  if ad['data'].has_key('sms_verification_required') :
   self._sms_verification_required= ad['data']['sms_verification_required'] 
  else:
   self._sms_verification_required = ''

  if ad['data'].has_key('temp_price') :
   self._temp_price= ad['data']['temp_price'] 
  else:
   self._temp_price = ''

  if ad['data'].has_key('temp_price_usd') :
   self._temp_price_usd= ad['data']['temp_price_usd'] 
  else:
   self._temp_price_usd = ''

  if ad['data'].has_key('track_max_amount') :
   self._track_max_amount= ad['data']['track_max_amount'] 
  else:
   self._track_max_amount = ''

  if ad['data'].has_key('trade_type') :
   self._trade_type= ad['data']['trade_type'] 
  else:
   self._trade_type = ''

  if ad['data'].has_key('trusted_required') :
   self._trusted_required= ad['data']['trusted_required'] 
  else:
   self._trusted_required = ''

  if ad['data'].has_key('visible') :
   self._visible= ad['data']['visible'] 
  else:
   self._visible = ''

  if ad['data'].has_key('volume_coefficient_btc') :
   self._volume_coefficient_btc= ad['data']['volume_coefficient_btc'] 
  else:
   self._volume_coefficient_btc = ''


 def dumps_update(self):
  dump = { 'price_equation' : self._price_equation, 
      'lat' : self._lat, 
      'lon' : self._lon, 
      'city' :  self._city, 
      'location_string' : self._location_string, 
      'countrycode' : self._countrycode,
      'currency' : self._currency, 
      'account_info' : self._account_info, 
      'bank_name' : self._bank_name, 
      'msg' : self._msg, 
      'sms_verification_required' :  self._sms_verification_required, 
      'track_max_amount' : self._track_max_amount, 
      'require_trusted_by_advertiser' : self._require_trusted_by_advertiser, 
      'require_identification' :  self._require_identification, 
      'min_amount' : self._min_amount, 
      'max_amount' : self._max_amount, 
      'opening_hours' : self._opening_hours, 
      'payment_window_minutes' : self._payment_window_minutes, 
      'visible' : self._visible }
  return dump

 def dumps_required(self):
  dump = { 'price_equation' : self._price_equation, 
      'lat' : self._lat, 
      'lon' : self._lon, 
      'city' :  self._city, 
      'location_string' : self._location_string, 
      'countrycode' : self._countrycode,
      'currency' : self._currency, 
      'account_info' : self._account_info, 
      'bank_name' : self._bank_name, 
      'msg' : self._msg, 
      'sms_verification_required' :  self._sms_verification_required, 
      'track_max_amount' : self._track_max_amount, 
      'require_trusted_by_advertiser' : self._require_trusted_by_advertiser, 
      'require_identification' :  self._require_identification}
  return dump

 def dumps_optional(self):
  dump = { 'price_equation' : self._price_equation, 
      'lat' : self._lat, 
      'lon' : self._lon, 
      'city' :  self._city, 
      'location_string' : self._location_string, 
      'countrycode' : self._countrycode,
      'currency' : self._currency, 
      'account_info' : self._account_info, 
      'bank_name' : self._bank_name, 
      'msg' : self._msg, 
      'sms_verification_required' :  self._sms_verification_required, 
      'track_max_amount' : self._track_max_amount, 
      'require_trusted_by_advertiser' : self._require_trusted_by_advertiser, 
      'require_identification' :  self._require_identification, 
      'min_amount' : self._min_amount, 
      'max_amount' : self._max_amount, 
      'opening_hours' : self._opening_hours} 
  return dump

 def dumps_online_buy(self):
  dump = { 'price_equation' : self._price_equation, 
      'lat' : self._lat, 
      'lon' : self._lon, 
      'city' :  self._city, 
      'location_string' : self._location_string, 
      'countrycode' : self._countrycode,
      'currency' : self._currency, 
      'account_info' : self._account_info, 
      'bank_name' : self._bank_name, 
      'msg' : self._msg, 
      'sms_verification_required' :  self._sms_verification_required, 
      'track_max_amount' : self._track_max_amount, 
      'require_trusted_by_advertiser' : self._require_trusted_by_advertiser, 
      'require_identification' :  self._require_identification, 
      'payment_window_minutes' : self._payment_window_minutes}
  return dump

 def dumps_online_buy_optional(self):
  dump = { 'price_equation' : self._price_equation, 
      'lat' : self._lat, 
      'lon' : self._lon, 
      'city' :  self._city, 
      'location_string' : self._location_string, 
      'countrycode' : self._countrycode,
      'currency' : self._currency, 
      'account_info' : self._account_info, 
      'bank_name' : self._bank_name, 
      'msg' : self._msg, 
      'sms_verification_required' :  self._sms_verification_required, 
      'track_max_amount' : self._track_max_amount, 
      'require_trusted_by_advertiser' : self._require_trusted_by_advertiser, 
      'require_identification' :  self._require_identification, 
      'min_amount' : self._min_amount, 
      'max_amount' : self._max_amount, 
      'opening_hours' : self._opening_hours, 
      'payment_window_minutes' : self._payment_window_minutes}
  return dump
