import Cookies from "js-cookie";

export const setCookie = (label: string, value: any) => {
    Cookies.set(label, value)
}

export const getCookie = (label:string) => {
    console.log(Cookies.get())
    const value = Cookies.get(label)
    if (value)
        return value
    else
        return false
}

export const delCookie = (label:string) => {
  Cookies.remove(label)
}

