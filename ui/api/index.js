import axios from 'axios';
import config from '@/config';

export function getUserInfoApi(jwt) {
  const path = `${config.schema}://${config.api.domain}:${config.api.port}`;
  const headers = { Authorization: `Bearer: ${jwt}` };
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
  return axios({
    method: 'post',
    url,
    data,
  });
}

export function registerUserApi(data) {
  const path = `${config.schema}://${config.api.domain}:${config.api.port}`;
  const url = `${path}/user/register`;
  return axios({
    method: 'post',
    url,
    data,
  });
}
