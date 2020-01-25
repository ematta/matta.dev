import axios from 'axios';

const path = process.env.VUE_APP_BASE_URL;

export function getUserInfoApi(jwt) {
  const headers = { Authorization: `Bearer: ${jwt}` };
  const url = `${path}/user/info`;
  return axios({
    method: 'get',
    url,
    headers,
  });
}

export function loginUserApi(data) {
  const url = `${path}/user/login`;
  return axios({
    method: 'post',
    url,
    data,
  });
}

export function registerUserApi(data) {
  const url = `${path}/user/register`;
  return axios({
    method: 'post',
    url,
    data,
  });
}
