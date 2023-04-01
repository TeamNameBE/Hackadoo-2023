function saveToken(token){
    localStorage.setItem('token', token);
}

function getToken(){
    return localStorage.getItem('token');
}

function saveRefreshToken(token){
    localStorage.setItem('refresh', token);
}

function getRefreshToken(){
    return localStorage.getItem('refresh');
}

function destroyToken(){
    localStorage.removeItem('token');
}

function destroyRefreshToken(){
    localStorage.removeItem('token');
}

module.exports = {
    saveToken,
    getToken,
    saveRefreshToken,
    getRefreshToken,
    destroyToken,
    destroyRefreshToken
}
