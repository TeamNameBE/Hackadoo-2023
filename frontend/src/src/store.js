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

function check_token(){
    if (localStorage.getItem('token') === null) {
        return false;
    }
    return true;
}

module.exports = {
    saveToken,
    getToken,
    saveRefreshToken,
    getRefreshToken,
    destroyToken,
    destroyRefreshToken,
    check_token
}
