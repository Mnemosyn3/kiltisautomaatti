export async function getTagNumber() {

    try{
        const response = await fetch('/getTagNumber');
        return await response.json();
    }catch(error) {
        return [];
    }
    
}

export async function GetUser(tagNumber) {

    try{
        const response = await fetch(`/getUser?tagNumber=${tagNumber}`);
        return await response.json();
    }catch(error) {
        return [];
    }
    
}