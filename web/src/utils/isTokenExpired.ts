import jwtDecode from 'jwt-decode'


function isTokenExpired(token: string) {
  const decodedToken: any = jwtDecode(token);
  const dateNow = new Date();

  if(decodedToken.exp * 1000 < dateNow.getTime())
      return true
  return false
}

export { isTokenExpired }
