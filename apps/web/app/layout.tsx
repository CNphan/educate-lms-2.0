import './style.css';
import type { ReactNode } from 'react';
export const metadata={title:'Educate LMS 2.0',description:'Multi-tenant learning management platform'};
export default function RootLayout({children}:{children:ReactNode}){return <html lang="en"><body>{children}</body></html>}
