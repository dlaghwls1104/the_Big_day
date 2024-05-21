/*
- 20230703 isGTMLoad 전역변수 추가
- 해당 변수는 페이지 내 GTM 스니펫 코드를 한 번만 로드하기 위한 용도입니다.
*/
let browserInfo = navigator.userAgent;
let isAndroid = browserInfo.indexOf('GA_Android') > -1;
let isIOS = browserInfo.indexOf('GA_iOS_WK') > -1;
let commonData = {};
let virCommonData = {};
let isGTMLoad = true;
window.dataLayer = window.dataLayer || [];

/*
- 매개변수 제거 함수
- 매개변수 값이 "" / null / undefined일 시 해당 필드를 객체에서 제거합니다.
*/
function removeEmptyElement(removeValue) {
  let returnValue = {};
  for (key in removeValue) {
    if (removeValue[key] === '' || removeValue[key] === null || removeValue[key] === undefined) {
      delete removeValue[key];
    }
  }
  returnValue = removeValue;

  return returnValue;
}

/*
- dataLayer 초기화 함수
- 해당 함수는 dataLayer를 초기화하여 이전 데이터의 중복 전송을 방지합니다.
*/
function resetDataLayer(targetObject) {
  let setGTM = {};
  for (key in targetObject) {
    setGTM[key] = undefined;
  }

  return dataLayer.push(setGTM);
}


/*
- 페이지뷰 전송 함수
- 화면 데이터를 전송합니다.
*/
function sendGAPage(object) {
  try {
    object = removeEmptyElement(object);
    commonData = { ...object };
    if (isAndroid || isIOS) {
      object.type = 'P';
      hybrid(object);
    } else {
        if (isGTMLoad) {
            (function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
            new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
            j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
            'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
            })(window,document,'script','dataLayer','GTM-W79MVWTM'); // GTM 추적코드 입력 바랍니다.  
            
            isGTMLoad = false;
        }
        object.event = 'ga_page';
        dataLayer.push(object);
        resetDataLayer(object);
    }
  } catch (e) {
    console.log('sendGAPage 함수 ERROR');
    console.log(e.message);
  }
}

/*
- 가상 페이지뷰 전송 함수
- 가상 페이지 데이터를 전송합니다.
- 해당 함수는 가상 페이지 전용 함수입니다.
*/
function sendGAVirPage(virObject) {
  try {
    virObject = removeEmptyElement(virObject);
    virCommonData = { ...virObject };
    virObject.event = 'ga_virtual';
    dataLayer.push(virObject);
    resetDataLayer(virObject);
  } catch (e) {
    console.log('sendVirPage 함수 ERROR');
    console.log(e.message);
  }
}

/*
- 이벤트 전송 함수 - 객체
- 해당 함수는 매개변수를 객체로 받아 사용합니다.
- 가상 페이지에서 사용 시 isVirtual 매개변수를 반드시 설정해야 합니다.
function sendGAEvent(object, isVirtual) {
  try {
    let GAData = removeEmptyElement(object);
    
    GAData.event = 'ga_event';
    isVirtual ? (GAData = { ...virCommonData, ...GAData }) : (GAData = { ...commonData, ...GAData });
    dataLayer.push(GAData);
    resetDataLayer(GAData);
  } catch (e) {
    console.log('sendGAEvent 함수 ERROR');
    console.log(e.message);
  }
}
*/
/*
- 이벤트 전송 함수 - 객체
- 앱과 웹 사용자를 구분하며, 이벤트 데이터를 전송합니다.
- 해당 함수는 매개변수를 객체로 받아 사용합니다.
*/


function sendGAEvent(object) {
  try {
    let GAData = removeEmptyElement(object);
    if (isAndroid || isIOS) {
      GAData.type = 'E';
      hybrid(GAData);
    } else {
      GAData.event = 'ga_event';
      isVirtual ? (GAData = { ...virCommonData, ...GAData }) : (GAData = { ...commonData, ...GAData });
      dataLayer.push(GAData);
      resetDataLayer(GAData);
    }
  } catch (e) {
    console.log('sendGAEvent 함수 ERROR');
    console.log(e.message);
  }
}


/*
- 이벤트 전송 함수 - 속성
- 해당 함수는 HTML attribute에서 이벤트 매개변수를 추출하여 데이터를 정의합니다.
- 가상 페이지에서 사용 시 isVirtual 매개변수를 반드시 설정해야 합니다.
*/
function sendGAAttrEvent(event, isVirtual) {
  try {
    const ELE = event.currentTarget;
    const ATTR = ELE.getAttributeNames();
    let GAData = {};
    for (var i = 0; i < ATTR.length; i++) {
      if (ATTR[i].includes('ep_')) {
        GAData[ATTR[i]] = ELE.getAttribute(ATTR[i]);
      }
    }
    GAData['event_name'] = ELE.getAttribute('event_name');

    GAData.event = 'ga_event';
    isVirtual ? (GAData = { ...virCommonData, ...GAData }) : (GAData = { ...commonData, ...GAData });
    dataLayer.push(GAData);
    resetDataLayer(GAData);

  } catch (e) {
    console.log('sendGAAttrEvent 함수 ERROR');
    console.log(e.message);
  }
}

/*
- 하이브리드 함수
- 앱사용자일 경우 데이터를 JSON 형태로 앱으로 전달합니다.
*/
function hybrid(object) {
  let GAData = { ...commonData, ...object };
  isAndroid ? window.mnetplusgascriptAndroid.GAHybrid(JSON.stringify(GAData)) : webkit.messageHandlers.mnetplusgascriptCallbackHandler.postMessage(JSON.stringify(GAData));
}