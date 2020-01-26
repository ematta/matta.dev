export function tokenGetExpireTime(token) {
  const data = JSON.parse(atob(token.split('.')[1]));
  return new Date(data.exp * 1000);
}

export function isValidToken(token) {
  if (!token || token.split('.').length < 3) {
    return false;
  }
  const exp = tokenGetExpireTime(token);
  const now = new Date();
  return now < exp;
}
