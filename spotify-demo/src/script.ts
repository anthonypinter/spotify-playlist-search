// this is auth code flow that needs to exist at the top of the script for
// the connection to Spotify to be made correctly

const clientId = "5fa292d4fc2d48d4aaaa20b221c7ff49"; // Replace with your client ID
const params = new URLSearchParams(window.location.search);
const code = params.get("code");
let accessToken: string;

if (!code) {
    redirectToAuthCodeFlow(clientId);
} else {
    accessToken = await getAccessToken(clientId, code);
}

// jukebox code starts below here

let counterElement = document.getElementById('counter');
let count = 0;
const lastKeysPressed: any = [];
let input: any = 0;
let queue: any = [];

function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }


async function player() {
    if (queue.length == 0) {
        return;
    }
    
    const playback = await currentlyPlaying(accessToken);
    if (playback["is_playing"] === false) {
        let track = queue.shift();
        data["uris"] = [track];
        sleep(5000); // this delays play, I think. In ms.
        
        play(accessToken, JSON.stringify(data));
        
    }
}

 // Get the counter element
 // const counterElement = document.getElementById("counter");

 // Add an event listener for keydown
 document.addEventListener("keydown", function(event) {
    if (/^[0-9]$/.test(event.key)) {
        // Increment the counter on numeric keypress
        count++;
        lastKeysPressed.push(event.key);
        counterElement.innerText += event.key;
    }
    if (event.key.toUpperCase() === "R") {
        // Reset the count when the "R" key is pressed
        count = 0;
        lastKeysPressed.length = 0;
        counterElement.innerText = '';
    }
   if (count === 3) {
    count = 0;
    
    input =  parseInt(lastKeysPressed[0] + "00") + parseInt(lastKeysPressed[1] + "0") + parseInt(lastKeysPressed[2]);
    
    const test = track_index.indexOf(input);
    if (test !== -1) {
        queue.push(tracks[test]);
        console.log(queue);
        
        
        //if (queue.length == 1) {
        //    player();
        //}
        // data["uris"] = [tracks[test]];
        //player(input, accessToken);
    }
    // console.log(test);
    // console.log(tracks[test]);
    // console.log(data)
    
    lastKeysPressed.length = 0;
    counterElement.innerText = ''
    //counterElement.innerText = count;
    
    }
 });

 const interval = setInterval(player, 2000);

 // this needs to be set to account for length of time for record to be picked and played (the 2000 number == 2 seconds)

 // 172 tracks currently -- index goes from 0 to 171
const tracks: string[]= ['spotify:track:0H8XeaJunhvpBdBFIYi6Sh', 'spotify:track:6QlkHjQmo2YncQN5MQXgPZ', 'spotify:track:7x8pIrhMu9FCmqqHNyuH0P', 'spotify:track:7sq2z9oX2S0CvgTqCZ0ko4', 'spotify:track:19aUuDd6udp1ACNo9t3IuZ', 'spotify:track:19YOJKCVvOL7v6B2Oe3UBc', 'spotify:track:45bE4HXI0AwGZXfZtMp8JR', 'spotify:track:40Fmr4mXhz4PtrMAPTnoXB', 'spotify:track:2EWpa5XnAuSn0sIkSSIhYk', 'spotify:track:4RVwu0g32PAqgUiJoXsdF8', 'spotify:track:0tbbtT3mRLAX7fPsSXR3hu', 'spotify:track:6Ng999MKVY9ikd8FtGaNnz', 'spotify:track:0ZAiqymvbQUZAh9y6ZT3Rm', 'spotify:track:6iCJCZqDJjmBxt07Oid6FI', 'spotify:track:7C2fjMlpeYTpaNyv7JuzBm', 'spotify:track:3I7krC8kr0gFR7P6vInR1I', 'spotify:track:1vrd6UOGamcKNGnSHJQlSt', 'spotify:track:6xGruZOHLs39ZbVccQTuPZ', 'spotify:track:427OHPoIWqO3SsFw77EkDf', 'spotify:track:49StY6V4Cus0xM0GhieSrT', 'spotify:track:4LDuSfbXupGKg6RpkgTAij', 'spotify:track:0Ky7dNE5kiSBgqNiwwl1jx', 'spotify:track:4EWCNWgDS8707fNSZ1oaA5', 'spotify:track:23c9gmiiv7RCu7twft0Mym', 'spotify:track:4h0EXpatqJImv4VRgvX6po', 'spotify:track:0qRE2t4scDRFsBgBXsQIH9', 'spotify:track:50a8bKqlwDEqeiEknrzkTO', 'spotify:track:0JXXNGljqupsJaZsgSbMZV', 'spotify:track:5Y3ID1NKAg8qydyVCrM7ji', 'spotify:track:1Fc2Gqn9bTuoeSHfhl1net', 'spotify:track:2ktg2oZDyFAX3iY1QNkXl5', 'spotify:track:2ZWlPOoWh0626oTaHrnl2a', 'spotify:track:5A7ldx7fFEEsHvl5XEnGUA', 'spotify:track:5Plx6OhvSukqCRdZ52wUXz', 'spotify:track:4SqWKzw0CbA05TGszDgMlc', 'spotify:track:5z75fXqSd5jhRsV543Trxh', 'spotify:track:3VByEy1Ax2hlDXgk2U9mmz', 'spotify:track:5411TEB6tlzvuF5A4oyldr', 'spotify:track:3HFBqhotJeEKHJzMEW31jZ', 'spotify:track:1luvsaicSpNDRLgOtRZxWO', 'spotify:track:2nUy0ifVE7UwtOK4rugFsP', 'spotify:track:1PDP7mLiAMwhfmgIwzhOm2', 'spotify:track:6K8VQ84MqhsoakN5MjrnVR', 'spotify:track:39KG4kom3enSx4GTThuDGt', 'spotify:track:6Se3x9ANMLv0dCDsjGmEjh', 'spotify:track:3yqXbpPYLuuL5p2lTQIsAB', 'spotify:track:5qrPtPZ0o6pXIwdJrzASTs', 'spotify:track:0vQcyuMEfRBd21ojZ62N2L', 'spotify:track:7aGyRfJWtLqgJaZoG9lJhE', 'spotify:track:4PRhg1fcYMevprYDkVqweI', 'spotify:track:7FIrk5lA1IalpZ3OtieeC8', 'spotify:track:7bFqfMKnKsZJH9FytUXg3E', 'spotify:track:4nVBt6MZDDP6tRVdQTgxJg', 'spotify:track:2xYUn5R79VRPW12pZKuwYd', 'spotify:track:2KN0Kgfb15aNLR0p2J4pkr', 'spotify:track:0QZ5yyl6B6utIWkxeBDxQN', 'spotify:track:7gDNQLV9cr8449LFrQbk5J', 'spotify:track:3oGbHF3Kdwf3AsRCbBjUxu', 'spotify:track:4THrHKyBL0yaDDw9yg37Zk', 'spotify:track:0GNVXNz7Jkicfk2mp5OyG5', 'spotify:track:3RIgHHpnFKj5Rni1shokDj', 'spotify:track:7MRyJPksH3G2cXHN8UKYzP', 'spotify:track:4Ro98RCK90oHqqSZUnTFq5', 'spotify:track:6KI1ZpZWYAJLvmVhCJz65G', 'spotify:track:2Xb6wJYGi0QXwURw5WWvI5', 'spotify:track:4FjPJhlEIWB9QVKFTc78Nn', 'spotify:track:2VYnlKxB8jpbCeLUjQsebc', 'spotify:track:3vcsq0fT4QN2B5UcSTvbZa', 'spotify:track:0w6webWdhjRKdqJ3DeGgM1', 'spotify:track:1MpQyTgfVMpUOnwKMTSMzu', 'spotify:track:1va84KD7DrxZ8U09Per4L8', 'spotify:track:4cKGldbhGJniI8BrB3K6tb', 'spotify:track:3AJwUDP919kvQ9QcozQPxg', 'spotify:track:0H6HlvjBoxXr2CBxQxa3lz', 'spotify:track:4fouWK6XVHhzl78KzQ1UjL', 'spotify:track:5RxpYHVbGJPOvSEATQyg9P', 'spotify:track:6tZ3b7ik1QDXFAZlXib0YZ', 'spotify:track:5icOoE6VgqFKohjWWNp0Ac', 'spotify:track:63xT6XPA0GtgzasSlRWjsj', 'spotify:track:3nsfB1vus2qaloUdcBZvDu', 'spotify:track:2KgGsmgnJiVV3oKYoHMKJk', 'spotify:track:5xDFYRukUOamdjnFoM3RoW', 'spotify:track:3uc8AGNL0KbvISIrjnfRvN', 'spotify:track:73YUReisjb3A9ActdLLjJQ', 'spotify:track:6m7Fh61cZbyoTTZBEllyAN', 'spotify:track:4Of7rzpRpV1mWRbhp5rAqG', 'spotify:track:6gjUxk2gNqaMtTYV0t3PPB', 'spotify:track:4WjTbrxOPvSwQlajlE4aXH', 'spotify:track:4AiFSXnVm0Bqecjdn3Brr8', 'spotify:track:5KSNxyuyp5K1kDT6LvX8oZ', 'spotify:track:4RCWB3V8V0dignt99LZ8vH', 'spotify:track:1KdouXr3rz8qZcvThrUyHC', 'spotify:track:4CkgMiMqZ5JzW9iYXSTMTL', 'spotify:track:6MYJv37Mpj5njLLbxKWNun', 'spotify:track:4U45aEWtQhrm8A5mxPaFZ7', 'spotify:track:6HU7h9RYOaPRFeh0R3UeAr', 'spotify:track:5IWMH89twdzA3XZpjW4Gvq', 'spotify:track:1jJci4qxiYcOHhQR247rEU', 'spotify:track:4EWBhKf1fOFnyMtUzACXEc', 'spotify:track:7uhKA1v3FnFouvVGmPkK5G', 'spotify:track:4pbG9SUmWIvsROVLF0zF9s', 'spotify:track:5BqW7B2eS98AlUAwW7EFLp', 'spotify:track:6J2LdBN97cDWn0MLxYh9HB', 'spotify:track:5hc71nKsUgtwQ3z52KEKQk', 'spotify:track:5gB2IrxOCX2j9bMnHKP38i', 'spotify:track:6xkryXuiZU360Lngd4sx13', 'spotify:track:27AJf1VXuh3h6QsqQBOLxf', 'spotify:track:7FXj7Qg3YorUxdrzvrcY25', 'spotify:track:4aT6vP9y2eDjxmRGm5ZqSC', 'spotify:track:6Kkt27YmFyIFrcX3QXFi2o', 'spotify:track:3GhsBdS9ulPK3KCdwHRPhG', 'spotify:track:5zCunX8URvLoBHlg1Fnjv6', 'spotify:track:6zeE5tKyr8Nu882DQhhSQI', 'spotify:track:3iNJUrTTqODoKapRzameCI', 'spotify:track:20fAoPjfYltmd3K3bO7gbt', 'spotify:track:1MONUudxAjEk76FJvzGhuD', 'spotify:track:78TzliRJJhCgsZ0ARUm8vI', 'spotify:track:5enxwA8aAbwZbf5qCHORXi', 'spotify:track:4Svpc4QRvDW0J34AE30S9c', 'spotify:track:1uMrc6mtKxqd5wLVzasmYA', 'spotify:track:56Qdvab5ordX97OCvgY3ie', 'spotify:track:27prib35GymFVzE8JLdA4u', 'spotify:track:02ppMPbg1OtEdHgoPqoqju', 'spotify:track:0NRHj8hDwwmSPaA41o379r', 'spotify:track:2d6m2F4I7wCuAKtSsdhh83', 'spotify:track:60wTHSJ0PxxwZDiSLiFaQX', 'spotify:track:0Tn997k4OPDZaT96R1MR8r', 'spotify:track:1HL3yEnYq8LEyFQ3QegA5V', 'spotify:track:4vHNeBWDQpVCmGbaccrRzi', 'spotify:track:7krbSH3rd8lhIZvuzTV3Bl', 'spotify:track:250RLekaiL1q9qZer975Eg', 'spotify:track:6mFkJmJqdDVQ1REhVfGgd1', 'spotify:track:29QSPMEVTvEtlgz3VrcoIU', 'spotify:track:3f3omU8n47Mqyab5nCaGyT', 'spotify:track:6AY1M1akbsVaQN3ATVyzH7', 'spotify:track:6Ey6LbYeaSQeVCIqAiKPKI', 'spotify:track:6xeTNdPnP5imNgDzFMfVfD', 'spotify:track:1vMGIZbIkpaLSagdF2ygcV', 'spotify:track:2nMeu6UenVvwUktBCpLMK9', 'spotify:track:7m9OqQk4RVRkw9JJdeAw96', 'spotify:track:42fw0rxRO2xbesF6mJfd4Y', 'spotify:track:6dBUzqjtbnIa1TwYbyw5CM', 'spotify:track:1LzNfuep1bnAUR9skqdHCK', 'spotify:track:1V4jC0vJ5525lEF1bFgPX2', 'spotify:track:0Om9WAB5RS09L80DyOfTNa', 'spotify:track:0MNNKSUU9OOQ8DSGWduw79', 'spotify:track:1yYlpGuBiRRf33e1gY61bN', 'spotify:track:6j7hih15xG2cdYwIJnQXsq', 'spotify:track:3rPtS4nfpy7PsARctAWpzd', 'spotify:track:5iVGN1Th2DqyWVNIBM8Vwk', 'spotify:track:1vqD0LaPZ3mgjRA7OUeXtf', 'spotify:track:4BXkf6yww23Vdju7E1fUrn', 'spotify:track:0NlGoUyOJSuSHmngoibVAs', 'spotify:track:3GCL1PydwsLodcpv0Ll1ch', 'spotify:track:4gikY8cxhdhFQ2xXsPPecy', 'spotify:track:258gfehYT0xOew1KasPadN', 'spotify:track:2dgFqt3w9xIQRjhPtwNk3D', 'spotify:track:40iHwasC0kEK8fgaEfQReF', 'spotify:track:2fhOljbX79loRcdl47SFye', 'spotify:track:2RwpoqhsYOZSGsF69KqjwP', 'spotify:track:1SDiiE3v2z89VxC3aVRKHQ', 'spotify:track:0HZhYMZOcUzZKSFwPOti6m', 'spotify:track:7D0RhFcb3CrfPuTJ0obrod', 'spotify:track:2zk7TQx9Xa4yxYmsjgDCPp', 'spotify:track:0ZUo4YjG4saFnEJhdWp9Bt', 'spotify:track:1ZwJALwnYbeHdEVCNVmniz', 'spotify:track:6xOt7VoZBPGQ9tTFpthuGQ', 'spotify:track:2lnF0JlRZQ12zPjwohhhYd', 'spotify:track:0YNtAadZvKBBEFARtfoCV8', 'spotify:track:1lbXEepatjRVjoG8pZMtdp', 'spotify:track:3aEAJmOonTPcvSdcWv0Y8s', 'spotify:track:748mdHapucXQri7IAO8yFK'];

const track_index: number[] = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271];


const data = {"uris": [],
};

async function play(token: string, data: string): Promise<any> {
    
    const result = await fetch("https://api.spotify.com/v1/me/player/play", {
        method: "PUT", 
        headers: { Authorization: `Bearer ${token}` },
        body: data
    });

    
}

async function currentlyPlaying(token: string): Promise<any> {
    
    const result = await fetch("https://api.spotify.com/v1/me/player/currently-playing", {
        method: "GET", 
        headers: { Authorization: `Bearer ${token}` }
        
    });
    return await result.json();
    
}

// everything below here is auth flow for hooking into Spotify API
// shouldn't need to touch this for the moment (10/27)

export async function redirectToAuthCodeFlow(clientId: string) {
    const verifier = generateCodeVerifier(128);
    const challenge = await generateCodeChallenge(verifier);

    localStorage.setItem("verifier", verifier);

    const params = new URLSearchParams();
    params.append("client_id", clientId);
    params.append("response_type", "code");
    params.append("redirect_uri", "http://localhost:5173/callback");
    params.append("scope", "user-read-private user-read-email user-modify-playback-state user-read-currently-playing");
    params.append("code_challenge_method", "S256");
    params.append("code_challenge", challenge);

    document.location = `https://accounts.spotify.com/authorize?${params.toString()}`;
}

function generateCodeVerifier(length: number) {
    let text = '';
    let possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    for (let i = 0; i < length; i++) {
        text += possible.charAt(Math.floor(Math.random() * possible.length));
    }
    return text;
}

async function generateCodeChallenge(codeVerifier: string) {
    const data = new TextEncoder().encode(codeVerifier);
    const digest = await window.crypto.subtle.digest('SHA-256', data);
    return btoa(String.fromCharCode.apply(null, [...new Uint8Array(digest)]))
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=+$/, '');
}

export async function getAccessToken(clientId: string, code: string): Promise<string> {
    const verifier = localStorage.getItem("verifier");

    const params = new URLSearchParams();
    params.append("client_id", clientId);
    params.append("grant_type", "authorization_code");
    params.append("code", code);
    params.append("redirect_uri", "http://localhost:5173/callback");
    params.append("code_verifier", verifier!);

    const result = await fetch("https://accounts.spotify.com/api/token", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: params
    });

    const { access_token } = await result.json();
    return access_token;
}

// below here is the code for the original Spotify demo to populate a page
// with information from a Spotify profile
// not needed any longer

/* function populateUI(profile: any) {
    document.getElementById("displayName")!.innerText = profile.display_name;
    if (profile.images[0]) {
        const profileImage = new Image(200, 200);
        profileImage.src = profile.images[0].url;
        document.getElementById("avatar")!.appendChild(profileImage);
    }
    document.getElementById("id")!.innerText = profile.id;
    document.getElementById("email")!.innerText = profile.email;
    document.getElementById("uri")!.innerText = profile.uri;
    document.getElementById("uri")!.setAttribute("href", profile.external_urls.spotify);
    document.getElementById("url")!.innerText = profile.href;
    document.getElementById("url")!.setAttribute("href", profile.href);
    document.getElementById("imgUrl")!.innerText = profile.images[0]?.url ?? '(no profile image)';

    
} */
