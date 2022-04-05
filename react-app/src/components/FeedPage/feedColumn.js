import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';

import './FeedPage.css';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCommentAlt, faHeart } from '@fortawesome/free-solid-svg-icons';
import PostModalPopup from '../Modals/PostModalPopup';

function FeedColumn({ column }) {
    return (
        <div className='posts-list'>
            {column.map(post => {

                return (
                    <div className='single-feed-post' key={post.id}>
                        <div className='post-image-div'>
                            <PostModalPopup post={post} />

                        </div>
                        <div className='post-info'>
                            <a href={`/users/${post.userId}/`}>
                                <div className='user-image-and-handle'>
                                    <img className='user-image' src={post.user.profileImageUrl} alt={post.user.id} />
                                    <p className='user-handle'>{post.user.handle}</p>
                                </div>
                            </a>
                            <div className='post-like-and-comment-count'>
                                <p className='post-like'
                                    style={{'color': '#818080', 'textAlign': 'center', 'top': '100%'}}
                                ><FontAwesomeIcon icon={faHeart} className={`feed__post__icon`} /> {post.postLikes.length}</p>
                                <p className='post-comment'
                                    style={{'color': '#818080', 'textAlign': 'center', 'marginBottom': '5px'}}
                                ><FontAwesomeIcon icon={faCommentAlt} className='feed__post__icon' /> 2</p>
                            </div>
                        </div>
                    </div>
                )
            })}
        </div>
    );
}

export default FeedColumn
