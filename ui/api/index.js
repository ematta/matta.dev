import axios from 'axios';
import config from '@/config';

export function checkIfLoggedInAlreadyApi(token) {
  const path = `${config.schema}://${config.api.domain}:${config.api.port}`;
  const headers = {
    Authorization: `Bearer: ${token}`,
    'Content-Type': 'application/json',
  };
  const url = `${path}/user/info`;
  return axios({
    method: 'get',
    url,
    headers,
  });
}

export function loginUserApi(data) {
  const path = `${config.schema}://${config.api.domain}:${config.api.port}`;
  const url = `${path}/user/login`;
  const headers = { 'Content-Type': 'application/json' };
  return axios({
    method: 'post',
    url,
    data,
    headers,
  });
}

export function registerUserApi(data) {
  const path = `${config.schema}://${config.api.domain}:${config.api.port}`;
  const url = `${path}/user/register`;
  const headers = { 'Content-Type': 'application/json' };
  return axios({
    method: 'post',
    url,
    data,
    headers,
  });
}
